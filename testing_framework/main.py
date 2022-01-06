class TestCase:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def run(self) -> None:
        getattr(self, self.name)()


class WasRun(TestCase):
    def __init__(self, name: str) -> None:
        self.was_run: bool = False

        super().__init__(name)

    def test_method(self) -> None:
        self.was_run: bool = True
