from .test_result import TestResult


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
