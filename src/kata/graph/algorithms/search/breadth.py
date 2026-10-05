from kata.graph.structures.vertex import Vertex
from kata.queue.structures.queue import Queue


def search[T](vertex: Vertex[T], value: T) -> Vertex[T] | None:
    """Find a value within the vertices reachable from `vertex` using
    breadth-first search.

    The time complexity of this operation is O(v + e).

    Parameters
    ----------
    vertex : Vertex[T]
        Starting vertex for the search.
    value : T
        Value to be found.

    Returns
    -------
    Vertex[T] | None
        Vertex containing the value to be found, or `None` if the value wasn't
        found.
    """
    seen = {vertex: True}
    queue: Queue[Vertex[T]] = Queue()
    queue.enqueue(vertex)
    while queue.peek() is not None:
        current = queue.deque()
        if current.value == value:
            return current
        for adjacent in current.adjacents:
            if adjacent not in seen:
                seen[adjacent] = True
                queue.enqueue(adjacent)
    return None
