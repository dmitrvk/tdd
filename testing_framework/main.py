class TestResult:
    def __init__(self) -> None:
        self.run_count: int = 0
        self.failure_count: int = 0

    def test_started(self) -> None:
        self.run_count += 1

    def test_failed(self) -> None:
        self.failure_count += 1

    def summary(self) -> str:
        return f'{self.run_count} run, {self.failure_count} failed'


class TestCase:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def set_up(self) -> None:
        ...

    def run(self, result: TestResult) -> TestResult:
        result.test_started()

        self.set_up()

        try:
            getattr(self, self.name)()
        except Exception:
            result.test_failed()

        self.tear_down()

    def tear_down(self) -> None:
        ...


class WasRun(TestCase):
    def set_up(self) -> None:
        self.log = 'set_up'

    def test_method(self) -> None:
        self.log += ' test_method'

    def test_broken_method(self) -> None:
        raise Exception()

    def tear_down(self) -> None:
        self.log += ' tear_down'


class TestSuite:
    def __init__(self) -> None:
        self.tests: list[WasRun] = []

    def add(self, test: WasRun) -> None:
        self.tests.append(test)

    def run(self, result: TestResult) -> None:
        for test in self.tests:
            test.run(result)
