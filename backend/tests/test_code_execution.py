import unittest
from app.services.executor import CodeExecutor
import time

class TestCodeExecutionSandbox(unittest.TestCase):
    def test_valid_python(self):
        executor = CodeExecutor(language='python', code='print("Hello LEARNX")')
        res = executor.execute()
        self.assertEqual(res['status'], 'success')
        self.assertEqual(res['stdout'].strip(), 'Hello LEARNX')
        self.assertEqual(res['error_type'], None)

    def test_valid_javascript(self):
        executor = CodeExecutor(language='javascript', code='console.log("Hello JS");')
        res = executor.execute()
        self.assertEqual(res['status'], 'success')
        self.assertEqual(res['stdout'].strip(), 'Hello JS')

    def test_python_syntax_error(self):
        executor = CodeExecutor(language='python', code='print("Missing bracket"')
        res = executor.execute()
        self.assertEqual(res['status'], 'runtime_error')
        self.assertEqual(res['error_type'], 'syntax_error')
        self.assertIn('SyntaxError', res['stderr'])

    def test_python_runtime_error(self):
        executor = CodeExecutor(language='python', code='1 / 0')
        res = executor.execute()
        self.assertEqual(res['status'], 'runtime_error')
        self.assertEqual(res['error_type'], 'zerodivisionerror')

    def test_python_timeout(self):
        # A simple infinite loop to trigger timeout
        executor = CodeExecutor(language='python', code='while True: pass', timeout_seconds=1.0)
        start = time.time()
        res = executor.execute()
        duration = time.time() - start
        
        self.assertEqual(res['status'], 'timeout')
        self.assertEqual(res['error_type'], 'timeout')
        # Ensure it didn't just hang indefinitely
        self.assertTrue(duration < 2.5)

    def test_invalid_language(self):
        executor = CodeExecutor(language='ruby', code='puts "hi"')
        res = executor.execute()
        self.assertEqual(res['status'], 'compile_error')
        self.assertEqual(res['error_type'], 'unsupported_language')

    def test_oversized_code(self):
        massive_code = "print('a')\n" * 6000 # Creates a file > 50KB
        executor = CodeExecutor(language='python', code=massive_code)
        res = executor.execute()
        self.assertEqual(res['status'], 'compile_error')
        self.assertEqual(res['error_type'], 'oversized_code')

    def test_oversized_stdin(self):
        massive_stdin = "input data " * 10000 # > 50KB
        executor = CodeExecutor(language='python', code="print(input())", stdin=massive_stdin)
        res = executor.execute()
        self.assertEqual(res['status'], 'compile_error')
        self.assertEqual(res['error_type'], 'oversized_stdin')
        
    def test_memory_limit_warning(self):
        executor = CodeExecutor(language='python', code='print("ok")')
        res = executor.execute()
        self.assertFalse(res['memory_limit_enforcement'])

if __name__ == '__main__':
    unittest.main()
