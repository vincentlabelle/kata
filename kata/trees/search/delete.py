from kata.trees.bnode import BNode


def delete[T](node: BNode[T], value: T) -> BNode[T] | None:
    """Delete `value` from the binary search tree represented by `node`.

    Parameters
    ----------
    node : BNode[T]
        Root of the binary search tree.
    value : T
        Value to delete.

    Raises
    ------
    TypeError
        Raised when `T` doesn't support the `<` operator.

    Returns
    -------
    BNode[T] | None
        Root of the new tree.
    """
    return _delete(node, value)


def _delete[T](node: BNode[T] | None, value: T) -> BNode[T] | None:
    if node is None:
        return None

    if node.value == value:
        return __delete(node)

    if node.value < value:  # type: ignore[operator]
        node.right = _delete(node.right, value)
    else:
        node.left = _delete(node.left, value)
    return node


def __delete[T](node: BNode[T]) -> BNode[T] | None:
    if node.left is None:
        return node.right
    if node.right is None:
        return node.left
    node.value = _maximum(node.left)
    node.left = _delete(node.left, node.value)
    return node


def _maximum[T](node: BNode[T]) -> T:
    if node.right is None:
        return node.value
    return _maximum(node.right)
