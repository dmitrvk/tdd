class TestCase:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def set_up(self) -> None:
        ...

    def run(self) -> None:
        self.set_up()
        getattr(self, self.name)()
        self.tear_down()

    def tear_down(self) -> None:
        ...


class WasRun(TestCase):
    def set_up(self) -> None:
        self.log = 'set_up'

    def test_method(self) -> None:
        self.log += ' test_method'

    def tear_down(self) -> None:
        self.log += ' tear_down'
