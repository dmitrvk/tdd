import abc
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .money import Money


class Expression(abc.ABC):
    @abc.abstractmethod
    def reduce(self, to: str) -> 'Money':
        ...

    @abc.abstractmethod
    def __add__(self, addend: 'Expression') -> 'Expression':
        ...

    @abc.abstractmethod
    def __mul__(self, multiplier: int) -> 'Expression':
        ...
