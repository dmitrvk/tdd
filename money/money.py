import abc


class Expression(abc.ABC):
    @abc.abstractmethod
    def reduce(self, to: str) -> 'Money':
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
    def amount(self) -> int:
        return self._amount

    @property
    def currency(self) -> str:
        return self._currency

    def times(self, multiplier: int) -> 'Money':
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend: 'Money') -> Expression:
        return Sum(self, addend)

    def reduce(self, to: str) -> 'Money':
        return self

    def __eq__(self, money: 'Money') -> bool:
        return (
            self._amount == money._amount
            and self.currency == money.currency
        )

    def __repr__(self) -> str:
        return f'<Money({self._amount}, {self._currency})>'


class Sum(Expression):
    def __init__(self, augend: Money, addend: Money) -> None:
        self._augend: Money = augend
        self._addend: Money = addend

    def reduce(self, to: str) -> Money:
        amount: int = self.augend.amount + self.addend.amount

        return Money(amount, to)

    @property
    def augend(self) -> Money:
        return self._augend

    @property
    def addend(self) -> Money:
        return self._addend


class Bank:
    def reduce(self, source: Expression, to: str) -> Money:
        return source.reduce(to)
