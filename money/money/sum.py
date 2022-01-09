from typing import TYPE_CHECKING

from .expression import Expression
from .money import Money

if TYPE_CHECKING:
    from .bank import Bank


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

    @property
    def augend(self) -> Money:
        return self._augend

    @property
    def addend(self) -> Money:
        return self._addend

    def __add__(self, addend: Expression) -> Expression:
        return Sum(self, addend)

    def __mul__(self, multiplier: int) -> Expression:
        return Sum(self.augend * multiplier, self.addend * multiplier)
