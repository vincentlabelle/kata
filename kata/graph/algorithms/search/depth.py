from kata.graph.structures.vertex import Vertex


def search[T](vertex: Vertex[T], value: T) -> Vertex[T] | None:
    """Find a value within the vertices reachable from `vertex` using
    depth-first search.

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
    return _search(vertex, value, {})


def _search[T](
    vertex: Vertex[T],
    value: T,
    seen: dict[Vertex[T], bool],
) -> Vertex[T] | None:
    if vertex.value == value:
        return vertex
    seen[vertex] = True
    for adjacent in vertex.adjacents:
        if adjacent not in seen:
            found = _search(adjacent, value, seen)
            if found is not None:
                return found
    return None
