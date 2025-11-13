import pytest

from kata.graph.algorithms.search.depth import search
from kata.graph.structures.vertex import Vertex


class TestSearch:
    @pytest.fixture(scope="function")
    def vertex(self) -> Vertex[int]:
        one, two, three, four, five, six, seven, eight, nine = (
            Vertex(1),
            Vertex(2),
            Vertex(3),
            Vertex(4),
            Vertex(5),
            Vertex(6),
            Vertex(7),
            Vertex(8),
            Vertex(9),
        )
        one.adjacents.append(two)
        one.adjacents.append(three)
        one.adjacents.append(eight)
        two.adjacents.append(one)
        two.adjacents.append(four)
        three.adjacents.append(five)
        three.adjacents.append(six)
        four.adjacents.append(seven)
        five.adjacents.append(six)
        six.adjacents.append(three)
        eight.adjacents.append(two)
        nine.adjacents.append(one)
        return one

    @pytest.mark.parametrize("value", [1, 2, 3, 4, 5, 6, 7, 8])
    def test_when_found(self, vertex: Vertex[int], value: int) -> None:
        found = search(vertex, value)
        assert found is not None
        assert found.value == value

    def test_when_not_found(self, vertex: Vertex[int]) -> None:
        assert search(vertex, 9) is None
