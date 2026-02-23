from kata.btree.structures.bnode import BNode


def paths_with_sum(node: BNode[int], target: int) -> int:
    """Given a binary tree, count the number of paths that sum to `target`.
    A path does not need to start or end at the root or a leaf, but it must
    go downwards.

    The algorithm must run in O(n) time.

    Parameters
    ----------
    node : BNode[int]
        Root of the tree.
    target : int
        Target sum.

    Returns
    -------
    int
        The count.
    """
    return _count(node, target, 0, {})


def _count(
    node: BNode[int] | None,
    target: int,
    previous: int,
    previouses: dict[int, int],
) -> int:
    if node is None:
        return 0
    current = previous + node.value
    count = previouses.get(current - target, 0)
    if current == target:
        count += 1
    previouses[current] = previouses.get(current, 0) + 1
    count += _count(node.left, target, current, previouses)
    count += _count(node.right, target, current, previouses)
    previouses[current] -= 1
    return count
