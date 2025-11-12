from kata.graph.structures.vertex import Vertex
from kata.queue.structures.queue import Queue


def traverse[T](vertex: Vertex[T]) -> list[T]:
    """Traverse the vertices connected to `vertex` using breadth-first search,
    and obtain the values.

    The time complexity of this operation is O(v + e).

    Parameters
    ----------
    vertex : Vertex[T]
        Starting vertex for the traversal.

    Returns
    -------
    list[T]
        The values contained in the connected graph starting at `vertex`.
    """
    seen = _traverse(vertex)
    return [v.value for v in seen]


def _traverse[T](vertex: Vertex[T]) -> dict[Vertex[T], bool]:
    seen = {vertex: True}
    queue: Queue[Vertex[T]] = Queue()
    queue.enqueue(vertex)
    while queue.peek() is not None:
        current = queue.deque()
        for adjacent in current.adjacents:
            if adjacent not in seen:
                seen[adjacent] = True
                queue.enqueue(adjacent)
    return seen
