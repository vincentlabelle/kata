import pytest

from kata.linked.problems.kth_to_last import kth_to_last
from kata.linked.structures.snode import SNode


class TestKthToLast:
    @pytest.mark.parametrize(
        "head, k, expected",
        [
            (SNode(0), -1, None),
            (SNode(0), 0, 0),
            (SNode(0), 1, None),
            (SNode(0, SNode(1)), -1, None),
            (SNode(0, SNode(1)), 0, 1),
            (SNode(0, SNode(1)), 1, 0),
            (SNode(0, SNode(1)), 2, None),
            (SNode(0, SNode(1, SNode(2))), -1, None),
            (SNode(0, SNode(1, SNode(2))), 0, 2),
            (SNode(0, SNode(1, SNode(2))), 1, 1),
            (SNode(0, SNode(1, SNode(2))), 2, 0),
            (SNode(0, SNode(1, SNode(2))), 3, None),
        ],
    )
    def test(self, head: SNode[int], k: int, expected: int | None) -> None:
        assert kth_to_last(head, k) == expected
