from .money import Franc, Money


class TestMoney:
    def test_multiplication(self) -> None:
        five = Money.dollar(5)

        assert five.times(2) == Money.dollar(10)
        assert five.times(3) == Money.dollar(15)

    def test_equality(self) -> None:
        assert Money.dollar(5) == Money.dollar(5)
        assert Money.dollar(5) != Money.dollar(6)
        assert Money.franc(5) == Money.franc(5)
        assert Money.franc(5) != Money.franc(6)
        assert Money.dollar(5) != Money.franc(5)

    def test_franc_multiplication(self) -> None:
        five = Money.franc(5)

        assert five.times(2) == Money.franc(10)
        assert five.times(3) == Money.franc(15)

    def test_currency(self) -> None:
        assert Money.dollar(1).currency == 'USD'
        assert Money.franc(1).currency == 'CHF'

    def test_different_class_euquailty(self) -> None:
        assert Money(10, 'CHF') == Franc(10, 'CHF')
