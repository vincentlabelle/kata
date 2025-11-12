import pytest

from kata.graph.algorithms.traverse.breadth import traverse
from kata.graph.structures.vertex import Vertex


class TestTraverse:
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

    def test(self, vertex: Vertex[int]) -> None:
        expected = [1, 2, 3, 8, 4, 5, 6, 7]
        actual = traverse(vertex)
        assert actual == expected
