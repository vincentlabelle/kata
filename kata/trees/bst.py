from typing import TypeVar

from kata.trees.bnode import BNode

T = TypeVar("T")


def exists(node: BNode[T], value: T) -> bool:
    """Verify if `value` is inside the binary search tree represented by `node`.
    The time complexity is between O(log(n)) and O(n).

    The time complexity is O(n) if the tree is one long branch (i.e., a linked
    list).

    Parameters
    ----------
    node : BNode[T]
        Root of the binary search tree.
    value : T
        Value to search for.

    Raises
    ------
    TypeError
        Raised when `T` doesn't support the `<` operator.

    Returns
    -------
    bool
        `True` if `value` is in the binary search tree, else `False`.
    """
    return _exists(node, value)


def _exists(node: BNode[T] | None, value: T) -> bool:
    if node is None:
        return False
    if node.value == value:
        return True
    if node.value < value:  # type: ignore[operator]
        return _exists(node.right, value)
    return _exists(node.left, value)
