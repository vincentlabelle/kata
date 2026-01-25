import pytest

from kata.linked.problems.sum_lists import sum_lists
from kata.linked.structures.snode import SNode


class TestSumLists:
    @pytest.mark.parametrize(
        "one, two, expected",
        [
            (
                SNode(1),
                SNode(2),
                SNode(3),
            ),
            (
                SNode(9),
                SNode(3),
                SNode(2, SNode(1)),
            ),
            (
                SNode(9),
                SNode(3, SNode(1)),
                SNode(2, SNode(2)),
            ),
            (
                SNode(3, SNode(1)),
                SNode(9),
                SNode(2, SNode(2)),
            ),
            (
                SNode(9, SNode(9, SNode(9))),
                SNode(3, SNode(1, SNode(2))),
                SNode(2, SNode(1, SNode(2, SNode(1)))),
            ),
        ],
    )
    def test(
        self,
        one: SNode[int],
        two: SNode[int],
        expected: SNode[int],
    ) -> None:
        actual = sum_lists(one, two)
        assert actual == expected
