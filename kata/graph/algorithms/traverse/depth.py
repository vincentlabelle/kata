from kata.graph.structures.vertex import Vertex


def traverse[T](vertex: Vertex[T]) -> list[T]:
    """Traverse the vertices reachable from `vertex` using depth-first search,
    and obtain the values.

    The time complexity of this operation is O(v + e).

    Parameters
    ----------
    vertex : Vertex[T]
        Starting vertex for the traversal.

    Returns
    -------
    list[T]
        The values contained in the vertices reachable from `vertex`.
    """
    seen: dict[Vertex[T], bool] = {}
    _traverse(vertex, seen)
    return [v.value for v in seen]


def _traverse[T](vertex: Vertex[T], seen: dict[Vertex[T], bool]) -> None:
    seen[vertex] = True
    for adjacent in vertex.adjacents:
        if adjacent not in seen:
            _traverse(adjacent, seen)
