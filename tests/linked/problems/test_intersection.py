import pytest

from kata.linked.problems.intersection import intersection
from kata.linked.structures.snode import SNode


class TestIntersection:
    _ONE = SNode(0)
    _TWO = SNode(0, SNode(1))

    @pytest.mark.parametrize(
        "one, two, expected",
        [
            (_ONE, _ONE, _ONE),
            (_ONE, SNode(0), None),
            (_ONE, SNode(1), None),
            (_TWO, _TWO, _TWO),
            (SNode(3, _TWO), _TWO, _TWO),
            (_TWO, SNode(3, _TWO), _TWO),
            (SNode(3, SNode(4, _TWO)), SNode(5, _TWO), _TWO),
            (SNode(3, SNode(4, _TWO)), SNode(5, SNode(6, _TWO)), _TWO),
            (SNode(0, SNode(1)), SNode(0, SNode(1)), None),
        ],
    )
    def test(
        self,
        one: SNode[int],
        two: SNode[int],
        expected: SNode[int] | None,
    ) -> None:
        assert intersection(one, two) is expected
