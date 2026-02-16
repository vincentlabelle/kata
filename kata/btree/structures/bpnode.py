from typing import Self


class BPNode[T]:
    """Representation of a node in a binary tree which holds a reference
    to its parent.

    Nodes are compared using referential equality.

    Parameters
    ----------
    value : T
        Value of the node.
    """

    def __init__(self, value: T) -> None:
        self.value = value
        self.parent: Self | None = None
        self.left: Self | None = None
        self.right: Self | None = None

    def __str__(self) -> str:
        return str(id(self))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self})"
