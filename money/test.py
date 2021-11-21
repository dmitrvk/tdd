from .money import Dollar


class TestMoney:
    def test_multiplication(self) -> None:
        five = Dollar(5)
        product = five.times(2)

        assert product.amount == 10

        product = five.times(3)

        assert product.amount == 15

    def test_equality(self) -> None:
        assert Dollar(5) == Dollar(5)
        assert Dollar(5) != Dollar(6)
