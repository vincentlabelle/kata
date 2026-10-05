"""Track integers to be able to periodically look up their rank. The rank of a
number x is the number of values less than or equal to x excluding x itself.

In other words, implement a function to track integers within a data structure,
and a function to retrieve the rank of an integer within the data structure.
Both operation must be optimized in terms of time.
"""

from typing import Self


class CNode:
    """Representation of a node in a binary tree. The node stores a count of
    its children in its left subtree in addition to a value.

    Parameters
    ----------
    value : int
        Value of the node.
    """

    def __init__(self, value: int) -> None:
        self.value = value
        self.count: int = 0
        self.left: Self | None = None
        self.right: Self | None = None

    def __str__(self) -> str:  # pragma: no cover
        return str(id(self))

    def __repr__(self) -> str:  # pragma: no cover
        return f"{self.__class__.__name__}({self})"


def track(value: int, node: CNode | None = None) -> CNode:
    """Track the rank of `value` by inserting it into a binary search tree.

    The algorithm runs in O(log(n)) time where `n` is the number of nodes if
    the binary search tree is balanced.

    Parameters
    ----------
    value : int
        Value to track.
    node : CNode | None
        Root of the binary search tree, defaults to `None`.

    Returns
    -------
    CNode
        The new root.
    """
    if node is None:
        return CNode(value)
    if value <= node.value:
        node.left = track(value, node.left)
        node.count += 1
    else:
        node.right = track(value, node.right)
    return node


def rank(value: int, node: CNode) -> int:
    """Get the rank of `value` in the binary search tree.

    The algorithm runs in O(log(n)) time where `n` is the number of nodes if
    the binary search tree is balanced.

    Parameters
    ----------
    value : int
        Value for which to get the rank.
    node : CNode
        Root of the binary search tree.

    Returns
    -------
    int
        Rank of `value`, or `-1` if `value` is not in the binary search tree.
    """
    if node.value == value:
        return node.count
    if value < node.value:
        if node.left is None:
            return -1
        return rank(value, node.left)
    else:
        if node.right is None:
            return -1
        rank_ = rank(value, node.right)
        if rank_ == -1:
            return -1
        return 1 + node.count + rank_
