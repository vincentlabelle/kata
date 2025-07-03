from kata.trees.bnode import BNode


def traverse[T](node: BNode[T]) -> list[T]:
    """Traverse the binary tree represented by `node`, and obtain the values
    it contains. The traversal is done using pre-order depth-first search. The
    time complexity is O(n).

    Parameters
    ----------
    node : BNode[T]
        The root node of the tree to traverse.

    Returns
    -------
    list[T]
        The values contained in the binary tree.
    """
    path: list[T] = []
    _traverse(node, path)
    return path


def _traverse[T](node: BNode[T] | None, path: list[T]) -> None:
    if node is None:
        return
    path.append(node.value)
    _traverse(node.left, path)
    _traverse(node.right, path)
