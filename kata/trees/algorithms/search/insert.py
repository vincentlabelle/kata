from kata.trees.structures.bnode import BNode


def insert[T](node: BNode[T], value: T) -> None:
    """Insert `value` inside the binary search tree represented by `node`.
    The time complexity is between O(log(n)) and O(n).

    Parameters
    ----------
    node : BNode[T]
        Root of the binary search tree.
    value : T
        Value to insert.

    Raises
    ------
    TypeError
        Raised when `T` doesn't support the `<` operator.
    """
    _insert(node, value)


def _insert[T](node: BNode[T] | None, value: T) -> BNode[T]:
    if node is None:
        return BNode(value)

    if node.value < value:  # type: ignore[operator]
        node.right = _insert(node.right, value)
    else:
        node.left = _insert(node.left, value)
    return node
