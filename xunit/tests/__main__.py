from xunit import TestSuite, TestResult
from .test_test_case import TestCaseTest


suite = TestSuite()
suite.add(TestCaseTest('test_template_method'))
suite.add(TestCaseTest('test_result'))
suite.add(TestCaseTest('test_failed_result'))
suite.add(TestCaseTest('test_failed_result_formatting'))
suite.add(TestCaseTest('test_suite'))

result = TestResult()

suite.run(result)

print(result.summary)
