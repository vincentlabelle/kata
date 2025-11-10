from collections.abc import MutableMapping
from typing import Iterator, Self


class TNode(MutableMapping[str, "TNode | None"]):
    """Representation of a node in a trie."""

    def __init__(self) -> None:
        self._map: dict[str, Self | None] = {}

    def __getitem__(self, key: str) -> Self | None:
        return self._map[key]

    def __setitem__(self, key: str, value: Self | None) -> None:
        self._map[key] = value

    def __delitem__(self, key: str) -> None:
        del self._map[key]

    def __len__(self) -> int:
        return len(self._map)

    def __iter__(self) -> Iterator[str]:
        return iter(self._map)

    def __eq__(self, other: object, /) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._map == other._map

    def __str__(self) -> str:
        return str(self._map)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self})"
