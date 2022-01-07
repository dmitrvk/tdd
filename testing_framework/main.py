class TestResult:
    def __init__(self) -> None:
        self.run_count: int = 0

    def test_started(self) -> None:
        self.run_count += 1

    def summary(self) -> str:
        return f'{self.run_count} run, 0 failed'


class TestCase:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def set_up(self) -> None:
        ...

    def run(self) -> TestResult:
        result = TestResult()
        result.test_started()

        self.set_up()
        getattr(self, self.name)()
        self.tear_down()

        return result

    def tear_down(self) -> None:
        ...


class WasRun(TestCase):
    def set_up(self) -> None:
        self.log = 'set_up'

    def test_method(self) -> None:
        self.log += ' test_method'

    def tear_down(self) -> None:
        self.log += ' tear_down'
