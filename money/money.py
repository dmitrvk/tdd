import abc


class Money(abc.ABC):
    def __init__(self, amount: int, currency: str) -> None:
        self._amount: int = amount
        self._currency = currency

    def __eq__(self, money: 'Money') -> bool:
        return (
            self._amount == money._amount
            and self.__class__ == money.__class__
        )

    @abc.abstractmethod
    def times(self, multiplier: int) -> 'Money':
        ...

    def currency(self) -> str:
        return self._currency

    @staticmethod
    def dollar(amount: int) -> 'Money':
        return Dollar(amount, 'USD')

    @staticmethod
    def franc(amount: int) -> 'Money':
        return Franc(amount, 'CHF')


class Dollar(Money):
    def times(self, multiplier: int) -> 'Money':
        return Money.dollar(self._amount * multiplier)


class Franc(Money):
    def times(self, multiplier: int) -> 'Money':
        return Money.franc(self._amount * multiplier)
