from .test_case import TestCase
from .test_result import TestResult


class TestSuite:
    def __init__(self) -> None:
        self._tests: list[TestCase] = []

    def add(self, test: TestCase) -> None:
        self._tests.append(test)

    def run(self, result: TestResult) -> None:
        for test in self._tests:
            test.run(result)
