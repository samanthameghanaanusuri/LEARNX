import os
import sys
import json
import subprocess
import tempfile

class WebCodeExecutor:
    """
    Evaluates HTML, CSS, and JS code securely using a headless Node.js environment (JSDOM).
    Hidden tests remain strictly on the backend.
    """
    
    def __init__(self, language, code, test_cases, timeout_seconds=5.0):
        self.language = language.lower()
        self.code = code
        self.test_cases = test_cases
        self.timeout_seconds = timeout_seconds

    def execute_all(self):
        """
        Executes all test cases in one Node.js process to minimize overhead.
        Returns a list of result dictionaries corresponding to the test cases.
        """
        results = []
        
        # Prepare the payload for the Node.js evaluator script
        payload = {
            'language': self.language,
            'code': self.code,
            'test_cases': [
                {
                    'id': tc.id,
                    'is_hidden': tc.is_hidden,
                    'input_data': tc.input_data,  # This will contain the JS validation logic string
                    'expected_output': tc.expected_output
                }
                for tc in self.test_cases
            ]
        }
        
        evaluator_script_path = os.path.join(os.path.dirname(__file__), '..', '..', 'evaluate_web.js')
        
        try:
            # We communicate via stdin/stdout using JSON
            process = subprocess.run(
                ['node', evaluator_script_path],
                input=json.dumps(payload),
                capture_output=True,
                text=True,
                timeout=self.timeout_seconds
            )
            
            if process.returncode != 0:
                # Runtime error in the evaluator script itself
                return self._fail_all(f"Runtime Error: {process.stderr}", 'runtime_error')
                
            # Parse the results
            try:
                node_results = json.loads(process.stdout)
                
                # Re-map node_results back to standard format
                for tc in self.test_cases:
                    tc_res_node = next((r for r in node_results if r['id'] == tc.id), None)
                    if not tc_res_node:
                        results.append(self._build_tc_error(tc, "Test case result missing from Node evaluator.", "runtime_error"))
                    else:
                        res = {
                            'test_case_id': tc.id,
                            'passed': tc_res_node.get('passed', False),
                            'status': tc_res_node.get('status', 'runtime_error'),
                            'execution_time_ms': tc_res_node.get('execution_time_ms', 0)
                        }
                        # Do not leak hidden test info
                        if not tc.is_hidden:
                            res['input'] = tc.input_data
                            res['expected'] = tc.expected_output
                            res['actual_stdout'] = tc_res_node.get('actual_stdout', '')
                            res['actual_stderr'] = tc_res_node.get('actual_stderr', '')
                        results.append(res)
                        
            except json.JSONDecodeError:
                return self._fail_all(f"Invalid JSON from evaluator. Output: {process.stdout}", 'runtime_error')
                
        except subprocess.TimeoutExpired:
            return self._fail_all("Execution timed out limit of 5.0s.", 'timeout')
        except Exception as e:
            return self._fail_all(f"Internal Executor Error: {str(e)}", 'runtime_error')
            
        return results

    def _fail_all(self, error_message, error_type):
        """Helper to fail all test cases if the whole executor script fails."""
        results = []
        for tc in self.test_cases:
            res = self._build_tc_error(tc, error_message, error_type)
            results.append(res)
        return results
        
    def _build_tc_error(self, tc, message, status):
        res = {
            'test_case_id': tc.id,
            'passed': False,
            'status': status,
            'execution_time_ms': 0
        }
        if not tc.is_hidden:
            res['input'] = tc.input_data
            res['expected'] = tc.expected_output
            res['actual_stdout'] = ""
            res['actual_stderr'] = message
        return res
