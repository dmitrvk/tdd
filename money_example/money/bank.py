from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .expression import Expression
    from .money import Money


class Bank:
    def __init__(self) -> None:
        self._rates: dict[tuple[str, str], int] = {}

    def reduce(self, source: 'Expression', to: str) -> 'Money':
        return source.reduce(self, to)

    def add_rate(self, from_: str, to: str, rate: int) -> None:
        self._rates[(from_, to)] = rate

    def rate(self, from_: str, to: str) -> int:
        if from_ == to:
            return 1

        return self._rates[(from_, to)]
