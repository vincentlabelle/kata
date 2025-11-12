from typing import Self


class Vertex[T]:
    """Representation of a vertex in a graph.

    Note that, after construction, the vertex has no adjacent vertices.
    Therefore, they must be added post-construction.

    Parameters
    ----------
    value : T
        Value of the vertex.
    """

    def __init__(self, value: T) -> None:
        self.value = value
        self.adjacents: list[Self] = []

    def __str__(self) -> str:
        return str(id(self))

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self})"
