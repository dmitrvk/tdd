from .fibonacci import fibonacci


def test_fibonacci() -> None:
    cases: dict[int, int] = {
        0: 0,
        1: 1,
    }

    for number, result in cases.items():
        assert fibonacci(number) == result
