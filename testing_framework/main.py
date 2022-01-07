class TestCase:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def set_up(self) -> None:
        ...

    def run(self) -> None:
        self.set_up()
        getattr(self, self.name)()


class WasRun(TestCase):
    def set_up(self) -> None:
        self.was_run: bool = False
        self.was_set_up: bool = True

    def test_method(self) -> None:
        self.was_run: bool = True
