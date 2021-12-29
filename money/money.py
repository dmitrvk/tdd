import abc


class Expression(abc.ABC):
    @abc.abstractmethod
    def reduce(self, to: str) -> 'Money':
        ...

    @abc.abstractmethod
    def plus(self, addend: 'Expression') -> 'Expression':
        ...

    @abc.abstractmethod
    def times(self, multiplier: int) -> 'Expression':
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

    def times(self, multiplier: int) -> Expression:
        return Money(self._amount * multiplier, self._currency)

    def plus(self, addend: Expression) -> Expression:
        return Sum(self, addend)

    def reduce(self, bank: 'Bank', to: str) -> 'Money':
        rate: int = bank.rate(self.currency, to)

        return Money(self.amount // rate, to)

    def __eq__(self, money: 'Money') -> bool:
        return (
            self._amount == money._amount
            and self.currency == money.currency
        )

    def __repr__(self) -> str:
        return f'<Money({self._amount}, {self._currency})>'


class Sum(Expression):
    def __init__(self, augend: Expression, addend: Expression) -> None:
        self._augend: Expression = augend
        self._addend: Expression = addend

    def reduce(self, bank: 'Bank', to: str) -> Money:
        amount: int = (
            self.augend.reduce(bank, to).amount
            + self.addend.reduce(bank, to).amount
        )

        return Money(amount, to)

    def plus(self, addend: Expression) -> Expression:
        return Sum(self, addend)

    def times(self, multiplier: int) -> Expression:
        return Sum(
            self.augend.times(multiplier),
            self.addend.times(multiplier),
        )

    @property
    def augend(self) -> Money:
        return self._augend

    @property
    def addend(self) -> Money:
        return self._addend


class Bank:
    def __init__(self) -> None:
        self._rates: dict[tuple[str, str], int] = {}

    def reduce(self, source: Expression, to: str) -> Money:
        return source.reduce(self, to)

    def add_rate(self, from_: str, to: str, rate: int) -> None:
        self._rates[(from_, to)] = rate

    def rate(self, from_: str, to: str) -> int:
        if from_ == to:
            return 1

        return self._rates[(from_, to)]
