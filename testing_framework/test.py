from main import TestCase, WasRun


class TestCaseTest(TestCase):
    def set_up(self) -> None:
        self.test = WasRun('test_method')

    def test_running(self) -> None:
        self.test.run()

        assert self.test.was_run

    def test_set_up(self) -> None:
        self.test.run()

        assert self.test.was_set_up


TestCaseTest('test_running').run()
TestCaseTest('test_set_up').run()
