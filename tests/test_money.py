from money import Bank, Expression, Money, Sum


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
        five = Money.dollar(5)
        sum_: Expression = five.plus(five)
        reduced = Bank().reduce(sum_, 'USD')

        assert reduced == Money.dollar(10)

    def test_plus_returns_sum(self) -> None:
        five = Money.dollar(5)
        result: Sum = five.plus(five)

        assert result.augend == five
        assert result.addend == five

    def test_reduce_sum(self) -> None:
        sum_: Expression = Sum(Money.dollar(3), Money.dollar(4))
        result: Money = Bank().reduce(sum_, 'USD')

        assert result == Money.dollar(7)

    def test_reduce_money_different_currency(self) -> None:
        bank = Bank()
        bank.add_rate('CHF', 'USD', 2)
        result = bank.reduce(Money.franc(2), 'USD')

        assert result == Money.dollar(1)

    def test_identity_rate(self) -> None:
        assert Bank().rate('USD', 'USD') == 1

    def test_mixed_addition(self) -> None:
        five_dollars = Money.dollar(5)
        ten_francs = Money.franc(10)

        bank = Bank()
        bank.add_rate('CHF', 'USD', 2)

        result = bank.reduce(five_dollars.plus(ten_francs), 'USD')

        assert result == Money.dollar(10)

    def test_sum_plus_money(self) -> None:
        five_dollars = Money.dollar(5)
        ten_francs = Money.franc(10)

        bank = Bank()
        bank.add_rate('CHF', 'USD', 2)

        sum_ = Sum(five_dollars, ten_francs).plus(five_dollars)

        result = bank.reduce(sum_, 'USD')

        assert result == Money.dollar(15)

    def test_sum_times(self) -> None:
        five_dollars = Money.dollar(5)
        ten_francs = Money.franc(10)

        bank = Bank()
        bank.add_rate('CHF', 'USD', 2)

        sum_ = Sum(five_dollars, ten_francs).times(2)

        result = bank.reduce(sum_, 'USD')

        assert result == Money.dollar(20)
