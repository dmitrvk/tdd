from xunit.xunit import TestCase


class WasRun(TestCase):
    def set_up(self) -> None:
        self.log = 'set_up'

    def test_method(self) -> None:
        self.log += ' test_method'

    def test_broken_method(self) -> None:
        raise Exception()

    def tear_down(self) -> None:
        self.log += ' tear_down'
