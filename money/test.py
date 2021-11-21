from .money import Dollar


class TestMoney:
    def test_multiplication(self) -> None:
        five = Dollar(5)

        assert five.times(2) == Dollar(10)
        assert five.times(3) == Dollar(15)

    def test_equality(self) -> None:
        assert Dollar(5) == Dollar(5)
        assert Dollar(5) != Dollar(6)
