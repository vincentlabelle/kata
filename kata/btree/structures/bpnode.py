from typing import Self


class BPNode[T]:
    """Representation of a node in a binary tree which holds a reference
    to its parent.

    Only the left and right child can be set on a node. The parent of the node
    is set automatically.

    Nodes are compared using referential equality.

    Parameters
    ----------
    value : T
        Value of the node.
    left : Self | None
        Left child of the node, defaults to `None`.
    right : Self | None
        Right child of the node, defaults to `None`.
    """

    def __init__(
        self,
        value: T,
        *,
        left: Self | None = None,
        right: Self | None = None,
    ) -> None:
        self._parent: Self | None = None
        self._left: Self | None = None
        self._right: Self | None = None
        self.value = value
        self.left = left
        self.right = right

    @property
    def parent(self) -> Self | None:
        """Self | None : The parent of this node."""
        return self._parent

    @property
    def left(self) -> Self | None:
        """Self | None : The left child of this node."""
        return self._left

    @left.setter
    def left(self, node: Self | None) -> None:
        self._unset_parent(self._left)
        self._left = node
        self._set_parent(self._left)

    def _unset_parent(self, node: Self | None) -> None:  # noqa: PLR6301
        if node is not None:
            node._parent = None

    def _set_parent(self, node: Self | None) -> None:
        if node is not None:
            self._unset_from_parent(node)
            node._parent = self

    def _unset_from_parent(self, node: Self) -> None:  # noqa: PLR6301
        previous = node._parent
        if previous is not None:
            if previous._left is node:
                previous._left = None
            else:
                previous._right = None

    @property
    def right(self) -> Self | None:
        """Self | None : The right child of this node."""
        return self._right

    @right.setter
    def right(self, node: Self | None) -> None:
        self._unset_parent(self._right)
        self._right = node
        self._set_parent(self._right)

    def __str__(self) -> str:
        return str(id(self))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self})"
