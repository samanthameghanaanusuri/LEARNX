import os
import sys
import tempfile
import subprocess
import time
import re

class CodeExecutor:
    """
    DEVELOPMENT ONLY FALLBACK RUNNER
    
    WARNING: 
    - This executor runs in local subprocesses.
    - It does NOT provide Docker-level or OS-level filesystem isolation on Windows.
    - Temporary directories DO NOT prevent a malicious script from reading/writing outside if they know the path.
    - It does NOT provide network isolation.
    - It does NOT provide memory limit enforcement.
    - Do NOT use this for untrusted public execution in production.
    """
    
    MAX_CODE_SIZE_BYTES = 50 * 1024  # 50 KB
    MAX_STDIN_SIZE_BYTES = 50 * 1024 # 50 KB

    SUPPORTED_LANGUAGES = {
        'python': {
            'ext': '.py',
            'cmd': [sys.executable],
        },
        'javascript': {
            'ext': '.js',
            'cmd': ['node'],
        },
        'java': {
            'ext': '.java',
            'cmd': ['java'],
        },
        'c': {
            'ext': '.c',
            'cmd': ['gcc'],
        }
    }

    def __init__(self, language, code, stdin=None, timeout_seconds=2.0):
        self.language = language.lower()
        self.code = code
        self.stdin = stdin if stdin else ""
        self.timeout_seconds = timeout_seconds

    def execute(self):
        # Enforce size limits
        if len(self.code.encode('utf-8')) > self.MAX_CODE_SIZE_BYTES:
            return self._build_error_response('compile_error', 'Code exceeds maximum size limit of 50KB.', 'oversized_code')
        if len(self.stdin.encode('utf-8')) > self.MAX_STDIN_SIZE_BYTES:
            return self._build_error_response('compile_error', 'Stdin exceeds maximum size limit of 50KB.', 'oversized_stdin')

        if self.language not in self.SUPPORTED_LANGUAGES:
            return self._build_error_response('compile_error', f'Unsupported language: {self.language}', 'unsupported_language')

        lang_config = self.SUPPORTED_LANGUAGES[self.language]
        
        # Create a temporary directory to isolate execution files
        with tempfile.TemporaryDirectory() as temp_dir:
            safe_env = {
                'PATH': os.environ.get('PATH', ''),
                'SystemRoot': os.environ.get('SystemRoot', ''),
                'SystemDrive': os.environ.get('SystemDrive', ''),
                'TEMP': os.environ.get('TEMP', ''),
                'TMP': os.environ.get('TMP', '')
            }

            if self.language == 'java':
                # Parse the public class name or first class name to name the .java file correctly
                match = re.search(r'public\s+class\s+([a-zA-Z0-9_]+)', self.code)
                if not match:
                    match = re.search(r'class\s+([a-zA-Z0-9_]+)', self.code)
                class_name = match.group(1) if match else 'Main'
                
                file_path = os.path.join(temp_dir, f"{class_name}.java")
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(self.code)
                
                # Compile stage: javac ClassName.java
                compile_cmd = ['javac', f"{class_name}.java"]
                try:
                    compile_process = subprocess.run(
                        compile_cmd,
                        capture_output=True,
                        text=True,
                        timeout=5.0,
                        cwd=temp_dir,
                        env=safe_env
                    )
                except subprocess.TimeoutExpired:
                    return self._build_error_response('compile_error', 'Compilation timed out.', 'compile_timeout')
                except Exception as e:
                    return self._build_error_response('compile_error', f'Compiler execution failed: {str(e)}', 'compiler_error')
                
                if compile_process.returncode != 0:
                    return self._build_error_response('compile_error', compile_process.stderr, 'compile_error')
                
                # Run stage: java ClassName
                cmd = ['java', class_name]
            elif self.language == 'c':
                file_path = os.path.join(temp_dir, "main.c")
                exe_name = "main.exe" if os.name == 'nt' else "main"
                exe_path = os.path.join(temp_dir, exe_name)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(self.code)
                
                # Compile stage: gcc main.c -o main.exe
                compile_cmd = ['gcc', "main.c", "-o", exe_name]
                try:
                    compile_process = subprocess.run(
                        compile_cmd,
                        capture_output=True,
                        text=True,
                        timeout=5.0,
                        cwd=temp_dir,
                        env=safe_env
                    )
                except FileNotFoundError:
                    return self._build_error_response('compile_error', 'Compiler execution failed: gcc not found on system.', 'compiler_error')
                except subprocess.TimeoutExpired:
                    return self._build_error_response('compile_error', 'Compilation timed out.', 'compile_timeout')
                except Exception as e:
                    return self._build_error_response('compile_error', f'Compiler execution failed: {str(e)}', 'compiler_error')
                
                if compile_process.returncode != 0:
                    return self._build_error_response('compile_error', compile_process.stderr, 'compile_error')
                
                # Run stage
                cmd = [f".\\{exe_name}" if os.name == 'nt' else f"./{exe_name}"]
            else:
                file_path = os.path.join(temp_dir, f"main{lang_config['ext']}")
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(self.code)
                cmd = lang_config['cmd'] + [file_path]
            
            start_time = time.time()
            try:
                process = subprocess.run(
                    cmd,
                    input=self.stdin,
                    capture_output=True,
                    text=True,
                    timeout=self.timeout_seconds,
                    cwd=temp_dir,
                    env=safe_env
                )
                
                exec_time_ms = int((time.time() - start_time) * 1000)
                
                if process.returncode == 0:
                    return {
                        'status': 'success',
                        'stdout': process.stdout,
                        'stderr': process.stderr,
                        'execution_time_ms': exec_time_ms,
                        'error_type': None,
                        'memory_limit_enforcement': False
                    }
                else:
                    return {
                        'status': 'runtime_error',
                        'stdout': process.stdout,
                        'stderr': process.stderr,
                        'execution_time_ms': exec_time_ms,
                        'error_type': self._classify_error(process.stderr, self.language),
                        'memory_limit_enforcement': False
                    }
                    
            except subprocess.TimeoutExpired as e:
                exec_time_ms = int((time.time() - start_time) * 1000)
                return {
                    'status': 'timeout',
                    'stdout': e.stdout.decode('utf-8') if (hasattr(e, 'stdout') and e.stdout) else '',
                    'stderr': f'Execution timed out after {self.timeout_seconds} seconds. Possible infinite loop.',
                    'execution_time_ms': exec_time_ms,
                    'error_type': 'timeout',
                    'memory_limit_enforcement': False
                }
            except Exception as e:
                exec_time_ms = int((time.time() - start_time) * 1000)
                return {
                    'status': 'runtime_error',
                    'stdout': '',
                    'stderr': str(e),
                    'execution_time_ms': exec_time_ms,
                    'error_type': 'system_error',
                    'memory_limit_enforcement': False
                }

    def _classify_error(self, stderr, language):
        if not stderr:
            return 'unknown_error'
            
        if language == 'python':
            if 'SyntaxError' in stderr or 'IndentationError' in stderr:
                return 'syntax_error'
            elif 'TypeError' in stderr:
                return 'type_error'
            elif 'NameError' in stderr:
                return 'name_error'
            elif 'IndexError' in stderr:
                return 'index_error'
            else:
                match = re.search(r'([A-Z][a-zA-Z0-9_]*Error):', stderr)
                if match:
                    return match.group(1).lower()
                return 'runtime_error'
                
        elif language == 'javascript':
            if 'SyntaxError' in stderr:
                return 'syntax_error'
            elif 'TypeError' in stderr:
                return 'type_error'
            elif 'ReferenceError' in stderr:
                return 'name_error'
            else:
                return 'runtime_error'
                
        elif language == 'java':
            if 'NullPointerException' in stderr:
                return 'nullpointerexception'
            elif 'ArrayIndexOutOfBoundsException' in stderr:
                return 'arrayindexoutofboundsexception'
            elif 'ArithmeticException' in stderr:
                return 'arithmeticexception'
            elif 'NumberFormatException' in stderr:
                return 'numberformatexception'
            else:
                match = re.search(r'java\.lang\.([a-zA-Z0-9_]+Exception)', stderr)
                if match:
                    return match.group(1).lower()
                return 'runtime_error'
                
        return 'runtime_error'

    def _build_error_response(self, status, stderr, error_type):
        return {
            'status': status,
            'stdout': '',
            'stderr': stderr,
            'execution_time_ms': 0,
            'error_type': error_type,
            'memory_limit_enforcement': False
        }
