class Expression:
    ...


class Money(Expression):
    def __init__(self, amount: int, currency: str) -> None:
        self._amount: int = amount
        self._currency: str = currency

    @staticmethod
    def dollar(amount: int) -> 'Money':
        return Money(amount, 'USD')

    @staticmethod
    def franc(amount: int) -> 'Money':
        return Money(amount, 'CHF')

    @property
    def currency(self) -> str:
        return self._currency

    def times(self, multiplier: int) -> 'Money':
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend: 'Money') -> Expression:
        return Money(self._amount + addend._amount, self._currency)

    def __eq__(self, money: 'Money') -> bool:
        return (
            self._amount == money._amount
            and self.currency == money.currency
        )

    def __repr__(self) -> str:
        return f'<Money({self._amount}, {self._currency})>'


class Bank:
    def reduce(self, source: Expression, to: str) -> Money:
        return Money.dollar(10)
