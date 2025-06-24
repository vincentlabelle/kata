from typing import Self


class SNode[T]:
    """Representation of a node in a singly linked list.

    Parameters
    ----------
    value : T
        Value of the node.
    next_ : Self | None
        Next node in the linked list.
    """

    def __init__(self, value: T, next_: Self | None = None) -> None:
        self.value = value
        self.next = next_

    def __eq__(self, other: object, /) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self.value == other.value and self.next == other.next

    def __str__(self) -> str:
        if self.next is None:
            return str(self.value)
        return f"{self.value}->{self.next}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self})"
