class Money:
    def __init__(self, amount: int) -> None:
        self._amount: int = amount

    def __eq__(self, money: 'Money') -> bool:
        return self._amount == money._amount


class Dollar(Money):
    def times(self, multiplier: int) -> 'Dollar':
        return Dollar(self._amount * multiplier)


class Franc(Money):
    def times(self, multiplier: int) -> 'Franc':
        return Franc(self._amount * multiplier)
