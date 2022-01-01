from .fibonacci import fibonacci


def test_fibonacci() -> None:
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
