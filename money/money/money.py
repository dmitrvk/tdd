from typing import TYPE_CHECKING

from .currency import Currency
from .expression import Expression

if TYPE_CHECKING:
    from .bank import Bank


class Money(Expression):
    def __init__(self, amount: int, currency: str) -> None:
        self._amount: int = amount
        self._currency: str = currency

    @staticmethod
    def dollar(amount: int) -> 'Money':
        return Money(amount, Currency.USD)

    @staticmethod
    def ruble(amount: int) -> 'Money':
        return Money(amount, Currency.RUB)

    @property
    def amount(self) -> int:
        return self._amount

    @property
    def currency(self) -> str:
        return self._currency

    def reduce(self, bank: 'Bank', to: str) -> 'Money':
        rate: int = bank.rate(self.currency, to)

        return Money(self.amount // rate, to)

    def __add__(self, addend: Expression) -> Expression:
        from .sum import Sum

        return Sum(self, addend)

    def __mul__(self, multiplier: int) -> Expression:
        return Money(self._amount * multiplier, self._currency)

    def __eq__(self, money: 'Money') -> bool:
        return (
            self._amount == money._amount
            and self.currency == money.currency
        )

    def __repr__(self) -> str:
        return f'<Money({self._amount}, {self._currency})>'
