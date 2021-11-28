import abc


class Money(abc.ABC):
    def __init__(self, amount: int, currency: str) -> None:
        self._amount: int = amount
        self._currency = currency

    def times(self, multiplier: int) -> 'Money':
        return Money(self._amount * multiplier, self._currency)

    @property
    def currency(self) -> str:
        return self._currency

    @staticmethod
    def dollar(amount: int) -> 'Money':
        return Dollar(amount, 'USD')

    @staticmethod
    def franc(amount: int) -> 'Money':
        return Franc(amount, 'CHF')

    def __eq__(self, money: 'Money') -> bool:
        return (
            self._amount == money._amount
            and self.currency == money.currency
        )

    def __repr__(self) -> str:
        return f'<Money({self._amount}, {self._currency})>'


class Dollar(Money):
    ...


class Franc(Money):
    ...
