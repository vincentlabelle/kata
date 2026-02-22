from kata.btree.structures.bnode import BNode


def is_subtree[T](one: BNode[T], two: BNode[T]) -> bool:
    """Given the two binary trees `one` and `two`, determine if `two` is a
    subtree of `one`. `two` is considered a subtree of `one` if there exists
    a node in `one` that is structurally identical to `two`.

    The algorithm must run in O(n * m).

    Parameters
    ----------
    one : BNode[T]
        First binary tree.
    two : BNode[T]
        Second binary tree.

    Returns
    -------
    bool
        `True` if `two` is a subtree of `one`, else `False`.
    """
    return _contains(one, two)


def _contains[T](one: BNode[T] | None, two: BNode[T]) -> bool:
    if one is None:
        return False
    return one == two or _contains(one.left, two) or _contains(one.right, two)
