class Dollar:
    def __init__(self, amount: int) -> None:
        self._amount: int = amount

    def times(self, multiplier: int) -> 'Dollar':
        return Dollar(self._amount * multiplier)

    def __eq__(self, dollar: 'Dollar') -> bool:
        return self._amount == dollar._amount
