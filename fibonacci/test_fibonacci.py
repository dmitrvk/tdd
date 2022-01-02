from .fibonacci import fibonacci


def test_fibonacci() -> None:
    cases: dict[int, int] = {
        0: 0,
        1: 1,
        2: 1,
        3: 2,
    }

    for number, result in cases.items():
        assert fibonacci(number) == result
