from main import TestCase, TestResult, WasRun


class TestCaseTest(TestCase):
    def test_template_method(self) -> None:
        test = WasRun('test_method')
        test.run()

        assert test.log == 'set_up test_method tear_down'

    def test_result(self) -> None:
        test = WasRun('test_method')
        result = test.run()

        assert result.summary() == '1 run, 0 failed'

    def test_failed_result(self) -> None:
        test = WasRun('test_broken_method')
        result = test.run()

        assert result.summary() == '1 run, 1 failed'

    def test_failed_result_formatting(self) -> None:
        result = TestResult()
        result.test_started()
        result.test_failed()

        assert result.summary() == '1 run, 1 failed'


TestCaseTest('test_template_method').run()
TestCaseTest('test_result').run()
TestCaseTest('test_failed_result').run()
TestCaseTest('test_failed_result_formatting').run()
