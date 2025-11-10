from kata.btrees.structures.bnode import BNode


def add[T](node: BNode[T], value: T) -> None:
    """Add `value` to the binary search tree represented by `node`.
    The time complexity is between O(log(n)) and O(n).

    Parameters
    ----------
    node : BNode[T]
        Root of the binary search tree.
    value : T
        Value to add.

    Raises
    ------
    TypeError
        Raised when `T` doesn't support the `<` operator.
    """
    _add(node, value)


def _add[T](node: BNode[T] | None, value: T) -> BNode[T]:
    if node is None:
        return BNode(value)

    if node.value < value:  # type: ignore[operator]
        node.right = _add(node.right, value)
    else:
        node.left = _add(node.left, value)
    return node
