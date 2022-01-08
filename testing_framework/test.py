from main import TestCase, TestResult, TestSuite, WasRun


class TestCaseTest(TestCase):
    def set_up(self) -> None:
        self.result = TestResult()

    def test_template_method(self) -> None:
        test = WasRun('test_method')
        test.run(self.result)

        assert test.log == 'set_up test_method tear_down'

    def test_result(self) -> None:
        test = WasRun('test_method')
        test.run(self.result)

        assert self.result.summary() == '1 run, 0 failed'

    def test_failed_result(self) -> None:
        test = WasRun('test_broken_method')
        test.run(self.result)

        assert self.result.summary() == '1 run, 1 failed'

    def test_failed_result_formatting(self) -> None:
        self.result.test_started()
        self.result.test_failed()

        assert self.result.summary() == '1 run, 1 failed'

    def test_suite(self) -> None:
        suite = TestSuite()
        suite.add(WasRun('test_method'))
        suite.add(WasRun('test_broken_method'))
        suite.run(self.result)

        assert self.result.summary() == '2 run, 1 failed'


suite = TestSuite()
suite.add(TestCaseTest('test_template_method'))
suite.add(TestCaseTest('test_result'))
suite.add(TestCaseTest('test_failed_result'))
suite.add(TestCaseTest('test_failed_result_formatting'))
suite.add(TestCaseTest('test_suite'))

result = TestResult()

suite.run(result)

print(result.summary())
