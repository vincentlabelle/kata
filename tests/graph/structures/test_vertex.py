import pytest

from kata.graph.structures.vertex import Vertex


@pytest.fixture(scope="function")
def vertex() -> Vertex[int]:
    one = Vertex(1)
    two = Vertex(2)
    one.adjacents.append(two)
    two.adjacents.append(one)
    return one


class TestVertexStr:
    def test(self, vertex: Vertex[int]) -> None:
        assert str(vertex) == str(id(vertex))


class TestVertexRepr:
    def test(self, vertex: Vertex[int]) -> None:
        expected = f"{vertex.__class__.__name__}({vertex})"
        assert repr(vertex) == expected
