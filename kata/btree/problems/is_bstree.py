from kata.btree.structures.bnode import BNode


def is_bstree(node: BNode[int]) -> bool:
    """Verify if a binary tree is a binary search tree.

    The algorithm must run in O(n) time.

    Parameters
    ----------
    node : BNode[int]
        The root of the tree to verify for.

    Returns
    -------
    bool
        `True` if the tree is a binary search tree, else `False`.
    """
    return _is_bstree(node, None, None)


def _is_bstree(
    node: BNode[int] | None,
    min_: int | None,
    max_: int | None,
) -> bool:
    if node is None:
        return True
    return (
        __is_bstree(node, min_, max_)
        and _is_bstree(node.left, min_, node.value)
        and _is_bstree(node.right, node.value, max_)
    )


def __is_bstree(node: BNode[int], min_: int | None, max_: int | None) -> bool:
    min__ = min_ is None or node.value > min_
    max__ = max_ is None or node.value <= max_
    return min__ and max__
