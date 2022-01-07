from main import TestCase, WasRun


class TestCaseTest(TestCase):
    def test_template_method(self) -> None:
        test = WasRun('test_method')
        test.run()

        assert test.log == 'set_up test_method tear_down'


TestCaseTest('test_template_method').run()
