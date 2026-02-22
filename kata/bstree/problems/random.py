from random import randrange

from kata.btree.structures.bnode import BNode


def random[T](node: BNode[T]) -> T:
    """Get a random value from a binary search tree.

    The algorithm must run in O(n) time.

    Note that it's possible to achieve a runtime of O(log(n)) if we can modify
    the attributes of `BNode`.

    Parameters
    ----------
    node : BNode[T]
        Root of the tree.

    Returns
    -------
    T
        The random value.
    """
    all_: list[T] = []
    _traverse(node, all_)
    index = randrange(0, len(all_))  # noqa: S311
    return all_[index]


def _traverse[T](node: BNode[T] | None, all_: list[T]) -> None:
    if node is None:
        return
    _traverse(node.left, all_)
    all_.append(node.value)
    _traverse(node.right, all_)
