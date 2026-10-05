from kata.btree.structures.bnode import BNode
from kata.queue.structures.queue import Queue


def list_depths(node: BNode[int]) -> list[list[int]]:
    """Given a binary tree, create a list of values for each level.

    The algorithm must run in O(n) time.

    Parameters
    ----------
    node : BNode[int]
        The root of the tree.

    Returns
    -------
    list[list[int]]
        The lists of values; one for each level.
    """
    depths: list[list[int]] = []
    queue: Queue[tuple[BNode[int], int]] = Queue()
    queue.enqueue((node, 0))
    while queue.peek() is not None:
        current, level = queue.deque()
        _append(depths, level, current.value)
        if current.left is not None:
            queue.enqueue((current.left, level + 1))
        if current.right is not None:
            queue.enqueue((current.right, level + 1))
    return depths


def _append(depths: list[list[int]], level: int, value: int) -> None:
    if level >= len(depths):
        depths.append([])
    depths[level].append(value)
