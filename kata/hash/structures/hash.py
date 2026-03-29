from collections.abc import MutableMapping
from typing import Iterator


class HashMap[KT, VT](MutableMapping[KT, VT]):
    """Representation of an hash map of `(KT, VT)` pairs.

    Parameters
    ----------
    capacity : int
        Capacity of the map.

    Raises
    ------
    ValueError
        Raised when `capacity` is negative or zero.
    """

    def __init__(self, capacity: int) -> None:
        self._capacity = capacity
        self._array: list[list[tuple[KT, VT]]] = [
            [] for _ in range(self._capacity)
        ]
        self._len = 0
        self._raise_if_capacity_is_negative_or_zero()

    def _raise_if_capacity_is_negative_or_zero(self) -> None:
        if self._capacity <= 0:
            message = (
                f"cannot create {self.__class__.__name__}; "
                + "capacity must be strictly positive"
            )
            raise ValueError(message)

    def __getitem__(self, key: KT) -> VT:  # type: ignore[return]
        # The time complexity of this operation is O(1) if there are no
        # collisions, otherwise it is O(n).
        inner = self._get(key)
        for k, v in inner:
            if k == key:
                return v
        self._raise_due_to_missing()

    def _get(self, key: KT) -> list[tuple[KT, VT]]:
        index = hash(key) % self._capacity
        return self._array[index]

    @staticmethod
    def _raise_due_to_missing() -> None:
        message = "cannot get item; key must be in map"
        raise KeyError(message)

    def __setitem__(self, key: KT, value: VT) -> None:
        # The time complexity of this operation is O(1) if there are no
        # collisions, otherwise it is O(n).
        pair = (key, value)
        inner = self._get(key)
        for i, (k, _) in enumerate(inner):
            if k == key:
                inner[i] = pair
                return
        inner.append(pair)
        self._len += 1

    def __delitem__(self, key: KT) -> None:
        # The time complexity of this operation is O(1) if there are no
        # collisions, otherwise it is O(n).
        inner = self._get(key)
        for i, (k, _) in enumerate(inner):
            if k == key:
                del inner[i]
                self._len -= 1
                return
        self._raise_due_to_missing()

    def __len__(self) -> int:
        return self._len

    def __iter__(self) -> Iterator[KT]:
        return (k for k, _ in self._iter())

    def _iter(self) -> Iterator[tuple[KT, VT]]:
        for inner in self._array:
            for k, v in inner:
                yield k, v

    def __eq__(self, other: object, /) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._len == other._len and all(
            k in other and other[k] == v for k, v in self._iter()
        )

    def __str__(self) -> str:
        return f"{{{', '.join(f'{k}: {v}' for k, v in self._iter())}}}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self})"
