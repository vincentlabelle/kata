from kata.btree.structures.bnode import BNode


def is_balanced(node: BNode[int]) -> bool:
    """Verify if a binary tree is balanced. The tree is considered balanced if
    the heights of the two subtrees of any node never differ by more than one.

    The algorithm must run in O(n) time.

    Parameters
    ----------
    node : BNode[int]
        The root of the tree to verify.

    Returns
    -------
    bool
        `True` if the tree is balanced, else `False`.
    """
    return _is_balanced(node, {})


def _is_balanced(node: BNode[int] | None, memo: dict[int, int]) -> bool:
    if node is None:
        return True
    return (
        _is_balanced(node.left, memo)
        and _is_balanced(node.right, memo)
        and __is_balanced(node, memo)
    )


def __is_balanced(node: BNode[int], memo: dict[int, int]) -> bool:
    return abs(_height(node.left, memo) - _height(node.right, memo)) <= 1


def _height(node: BNode[int] | None, memo: dict[int, int]) -> int:
    if node is None:
        return 0
    if id(node) not in memo:
        height = max(_height(node.left, memo), _height(node.right, memo)) + 1
        memo[id(node)] = height
    return memo[id(node)]
