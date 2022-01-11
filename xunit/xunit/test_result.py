class TestResult:
    def __init__(self) -> None:
        self._run_count: int = 0
        self._failure_count: int = 0

    @property
    def summary(self) -> str:
        return f'{self._run_count} run, {self._failure_count} failed'

    def test_started(self) -> None:
        self._run_count += 1

    def test_failed(self) -> None:
        self._failure_count += 1
