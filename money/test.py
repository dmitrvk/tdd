from .money import Bank, Expression, Money


class TestMoney:
    def test_multiplication(self) -> None:
        five = Money.dollar(5)

        assert five.times(2) == Money.dollar(10)
        assert five.times(3) == Money.dollar(15)

    def test_equality(self) -> None:
        assert Money.dollar(5) == Money.dollar(5)
        assert Money.dollar(5) != Money.dollar(6)
        assert Money.dollar(5) != Money.franc(5)

    def test_currency(self) -> None:
        assert Money.dollar(1).currency == 'USD'
        assert Money.franc(1).currency == 'CHF'

    def test_simple_addition(self) -> None:
        sum_: Expression = Money.dollar(5).plus(Money.dollar(5))
        reduced = Bank().reduce(sum_, 'USD')

        assert reduced == Money.dollar(10)
