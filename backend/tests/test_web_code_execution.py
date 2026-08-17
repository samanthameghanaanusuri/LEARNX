import unittest
from app.services.web_executor import WebCodeExecutor

class MockTestCase:
    def __init__(self, id, is_hidden, input_data, expected_output):
        self.id = id
        self.is_hidden = is_hidden
        self.input_data = input_data
        self.expected_output = expected_output

class TestWebCodeExecution(unittest.TestCase):
    def test_html_dom_check(self):
        code = "<h1>Hello</h1>"
        tc = MockTestCase(id=1, is_hidden=False, input_data="return document.querySelector('h1').textContent === 'Hello';", expected_output="true")
        executor = WebCodeExecutor(language='html', code=code, test_cases=[tc])
        res = executor.execute_all()
        print("HTML Test Result:", res)
        self.assertEqual(len(res), 1)
        self.assertTrue(res[0]['passed'])
        self.assertEqual(res[0]['status'], 'success')

    def test_css_dom_check(self):
        code = "h1 { color: red; }"
        tc = MockTestCase(id=2, is_hidden=False, input_data="return true;", expected_output="true")
        executor = WebCodeExecutor(language='css', code=code, test_cases=[tc])
        res = executor.execute_all()
        print("CSS Test Result:", res)
        self.assertTrue(res[0]['passed'])

    def test_js_evaluation(self):
        code = "console.log('Log message');"
        tc = MockTestCase(id=3, is_hidden=False, input_data="return actualStdout.includes('Log message');", expected_output="true")
        executor = WebCodeExecutor(language='javascript', code=code, test_cases=[tc])
        res = executor.execute_all()
        print("JS Test Result:", res)
        self.assertTrue(res[0]['passed'])

if __name__ == '__main__':
    unittest.main()
