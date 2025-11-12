from kata.btrees.structures.bnode import BNode
from kata.queues.structures.queue import Queue


def traverse[T](node: BNode[T]) -> list[T]:
    """Traverse the binary tree repesented by `node`, and obtain the values
    it contains. The traversal is done using breadth-first search. The time
    complexity is O(n).

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

    queue: Queue[BNode[T]] = Queue()
    queue.enqueue(node)
    while queue.peek() is not None:
        current = queue.deque()
        path.append(current.value)
        if current.left is not None:
            queue.enqueue(current.left)
        if current.right is not None:
            queue.enqueue(current.right)

    return path
