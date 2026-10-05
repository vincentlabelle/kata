from kata.btree.structures.bnode import BNode


def all_arrays(node: BNode[int]) -> list[list[int]]:
    """Given a binary search tree which was created by traversing through an
    array from left to right, find all possible arrays that could have led
    to the tree.

    Parameters
    ----------
    node : BNode[int]
        Root of the tree.

    Returns
    -------
    list[list[int]]
        All the possible arrays.
    """
    all_: list[list[int]] = []
    _collect([], [node], all_)
    return all_


def _collect(
    array: list[int],
    next_: list[BNode[int]],
    all_: list[list[int]],
) -> None:
    if len(next_) == 0:
        all_.append(array)
    for current in next_:
        array_ = [*array, current.value]
        next__ = [n for n in next_ if n is not current]
        if current.left is not None:
            next__.append(current.left)
        if current.right is not None:
            next__.append(current.right)
        _collect(array_, next__, all_)
