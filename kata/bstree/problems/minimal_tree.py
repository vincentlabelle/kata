from kata.btree.structures.bnode import BNode


def minimal_tree(array: list[int]) -> BNode[int] | None:
    """Given a sorted array with unique integer elements, create a binary search
    tree with minimal height.

    The algorithm must run in O(n) time.

    Parameters
    ----------
    array : list[int]
        Array from which to create the tree.

    Returns
    -------
    BNode[int] | None
        The root node of the tree.
    """
    return _make(array, 0, len(array) - 1)


def _make(array: list[int], lower: int, upper: int) -> BNode[int] | None:
    if lower > upper:
        return None
    mid = (upper + lower) // 2
    node = BNode(array[mid])
    node.left = _make(array, lower, mid - 1)
    node.right = _make(array, mid + 1, upper)
    return node
