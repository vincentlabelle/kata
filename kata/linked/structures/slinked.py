from typing import Iterator

from kata.linked.structures.snode import SNode


class SLinked[T]:
    """Representation of a singly linked list of `T`."""

    def __init__(self) -> None:
        self._head: SNode[T] | None = None
        self._len = 0

    def insert(self, index: int, value: T) -> None:
        """Insert `value` before `index` in this list. The time complexity of
        this operation is O(1) if `index == 0`, otherwise it is O(n).

        Parameters
        ----------
        index : int
            Index before which to insert.
        value : T
            Value to insert.

        Raises
        ------
        IndexError
            Raised when `index` is outside [0, `len(self)`].
        """
        if index == 0:
            self.prepend(value)
        elif index == len(self):
            self.append(value)
        else:
            self._insert(index, value)

    def prepend(self, value: T) -> None:
        """Insert `value` at the beginning of this list. The time complexity of
        this operation is O(1).

        Parameters
        ----------
        value : T
            Value to insert.
        """
        new = SNode(value)
        if self._head is not None:
            new.next = self._head
        self._head = new
        self._len += 1

    def append(self, value: T) -> None:
        """Insert `value` at the end of this list. The time complexity of this
        operation is O(n).

        Parameters
        ----------
        value : T
            Value to insert.
        """
        new = SNode(value)
        if self._head is None:
            self._head = new
        else:
            _, node = self._traverse(len(self) - 1)
            node.next = new
        self._len += 1

    def _insert(self, index: int, value: T) -> None:
        new = SNode(value)
        previous, node = self._traverse(index)
        assert previous is not None  # noqa: S101
        previous.next = new
        new.next = node
        self._len += 1

    def _traverse(self, index: int) -> tuple[SNode[T] | None, SNode[T]]:
        self._raise_if_out_of_bounds(index)
        return self.__traverse(index)

    def _raise_if_out_of_bounds(self, index: int) -> None:
        if not 0 <= index < len(self):
            message = "cannot perform operation; index out of bounds"
            raise IndexError(message)

    def __traverse(self, index: int) -> tuple[SNode[T] | None, SNode[T]]:
        previous = None
        for i, node in enumerate(self._iter()):
            if i == index:
                return previous, node
            previous = node
        assert False  # noqa: S101 # pragma: no cover

    def __getitem__(self, index: int) -> T:
        # The time complexity of this operation is O(1) if `index == 0`,
        # otherwise it is O(n).
        _, node = self._traverse(index)
        return node.value

    def __setitem__(self, index: int, value: T) -> None:
        # The time complexity of this operation is O(1) if `index == 0`,
        # otherwise it is O(n).
        _, node = self._traverse(index)
        node.value = value

    def __delitem__(self, index: int) -> None:
        # The time complexity of this operation is O(1) if `index == 0`,
        # otherwise it is O(n).
        previous, node = self._traverse(index)
        if previous is None:
            self._head = node.next
        else:
            previous.next = node.next
        self._len -= 1

    def __len__(self) -> int:
        return self._len

    def __contains__(self, value: T) -> bool:
        # The time complexity of this operation is O(n).
        return any(v == value for v in self)

    def __iter__(self) -> Iterator[T]:
        return (node.value for node in self._iter())

    def _iter(self) -> Iterator[SNode[T]]:
        node = self._head
        while node is not None:
            yield node
            node = node.next

    def __eq__(self, other: object, /) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._head == other._head

    def __str__(self) -> str:
        if self._head is None:
            return "||"
        return f"|{self._head}|"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self})"
