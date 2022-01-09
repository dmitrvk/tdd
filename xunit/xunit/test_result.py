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
