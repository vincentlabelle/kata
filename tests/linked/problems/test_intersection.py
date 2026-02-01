import pytest

from kata.linked.problems.intersection import intersection
from kata.linked.structures.snode import SNode


class TestIntersection:
    @pytest.mark.parametrize(
        "one, two, expected",
        [
            (SNode(0), SNode(0), 0),
            (SNode(0), SNode(1), None),
            (SNode(0, SNode(1)), SNode(0, SNode(1)), 0),
            (SNode(0, SNode(1)), SNode(1, SNode(0)), 1),
            (SNode(0, SNode(1)), SNode(2, SNode(0)), 0),
            (SNode(0, SNode(1)), SNode(2, SNode(3)), None),
        ],
    )
    def test(self, one: SNode[int], two: SNode[int], expected: int) -> None:
        assert intersection(one, two) == expected
