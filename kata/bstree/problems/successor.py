from kata.btree.structures.bpnode import BPNode


def successor(node: BPNode[int]) -> int | None:
    """Given a node from a binary search tree, find the successor's value.
    The successor is the next node based on in-order traversal.

    The algorithm must run in O(h) time, where h is the height of the tree.

    Parameters
    ----------
    node : BPNode[int]
        Node for which to find the successor's value.

    Returns
    -------
    int | None
        The value of the successor, or `None` if there are no successor.
    """
    if node.right is None:
        return _successor_parent(node)
    return _successor_child(node.right)


def _successor_parent(node: BPNode[int]) -> int | None:
    if node.parent is None:
        return None
    if node.parent.left is node:
        return node.parent.value
    return _successor_parent(node.parent)


def _successor_child(node: BPNode[int]) -> int:
    if node.left is None:
        return node.value
    return _successor_child(node.left)
