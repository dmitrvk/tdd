from money import Dollar


class TestMoney:
    def test_multiplication(self) -> None:
        five = Dollar(5)
        five.times(2)
        assert five.amount == 10
