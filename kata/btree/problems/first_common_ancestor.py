from kata.btree.structures.bpnode import BPNode


def first_common_ancestor[T](
    node: BPNode[T],
    other: BPNode[T],
) -> BPNode[T] | None:
    """Find the first common ancestor of two nodes in a binary tree without
    using an additional data structure.

    The algorithm must run in O(n) time.

    Parameters
    ----------
    node : BPNode[T]
        First node for which to find the FCA.
    other : BPNode[T]
        Second node for which to find the FCA.

    Returns
    -------
    BPNode[T] | None
        The FCA, or `None` if none exists.
    """
    if _contains(node, other):
        return node
    return _search(node.parent, other, node)


def _contains[T](node: BPNode[T] | None, other: BPNode[T]) -> bool:
    if node is None:
        return False
    return (
        node is other
        or _contains(node.right, other)
        or _contains(node.left, other)
    )


def _search[T](
    node: BPNode[T] | None,
    other: BPNode[T],
    previous: BPNode[T],
) -> BPNode[T] | None:
    if node is None:
        return None
    if (
        node is other
        or (node.left is previous and _contains(node.right, other))
        or (node.right is previous and _contains(node.left, other))
    ):
        return node
    return _search(node.parent, other, node)
