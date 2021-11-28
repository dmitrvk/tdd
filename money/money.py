import abc


class Money(abc.ABC):
    def __init__(self, amount: int) -> None:
        self._amount: int = amount

    def __eq__(self, money: 'Money') -> bool:
        return (
            self._amount == money._amount
            and self.__class__ == money.__class__
        )

    @abc.abstractmethod
    def times(self, multiplier: int) -> 'Money':
        ...

    @staticmethod
    def dollar(amount: int) -> 'Money':
        return Dollar(amount)

    @staticmethod
    def franc(amount: int) -> 'Money':
        return Franc(amount)


class Dollar(Money):
    def times(self, multiplier: int) -> 'Money':
        return Dollar(self._amount * multiplier)


class Franc(Money):
    def times(self, multiplier: int) -> 'Money':
        return Franc(self._amount * multiplier)
