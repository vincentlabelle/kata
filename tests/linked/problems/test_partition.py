import pytest

from kata.linked.problems.partition import partition
from kata.linked.structures.snode import SNode


class TestPartition:
    @pytest.mark.parametrize(
        "head, value, expected",
        [
            (SNode(1), 0, SNode(1)),
            (SNode(1), 1, SNode(1)),
            (SNode(1), 2, SNode(1)),
            (SNode(1, SNode(2)), 0, SNode(1, SNode(2))),
            (SNode(1, SNode(2)), 1, SNode(1, SNode(2))),
            (SNode(1, SNode(2)), 2, SNode(1, SNode(2))),
            (SNode(1, SNode(2)), 3, SNode(1, SNode(2))),
            (SNode(2, SNode(1)), 0, SNode(2, SNode(1))),
            (SNode(2, SNode(1)), 1, SNode(2, SNode(1))),
            (SNode(2, SNode(1)), 2, SNode(1, SNode(2))),
            (SNode(2, SNode(1)), 3, SNode(2, SNode(1))),
            (SNode(1, SNode(2, SNode(3))), 0, SNode(1, SNode(2, SNode(3)))),
            (SNode(1, SNode(2, SNode(3))), 1, SNode(1, SNode(2, SNode(3)))),
            (SNode(1, SNode(2, SNode(3))), 2, SNode(1, SNode(2, SNode(3)))),
            (SNode(1, SNode(2, SNode(3))), 3, SNode(1, SNode(2, SNode(3)))),
            (SNode(1, SNode(2, SNode(3))), 4, SNode(1, SNode(2, SNode(3)))),
            (SNode(3, SNode(2, SNode(1))), 0, SNode(3, SNode(2, SNode(1)))),
            (SNode(3, SNode(2, SNode(1))), 1, SNode(3, SNode(2, SNode(1)))),
            (SNode(3, SNode(2, SNode(1))), 2, SNode(1, SNode(2, SNode(3)))),
            (SNode(3, SNode(2, SNode(1))), 3, SNode(2, SNode(1, SNode(3)))),
            (SNode(3, SNode(2, SNode(1))), 4, SNode(3, SNode(2, SNode(1)))),
            (SNode(2, SNode(3, SNode(1))), 2, SNode(1, SNode(3, SNode(2)))),
            (SNode(2, SNode(3, SNode(1))), 3, SNode(2, SNode(1, SNode(3)))),
        ],
    )
    def test(self, head: SNode[int], value: int, expected: SNode[int]) -> None:
        partition(head, value)
        assert head == expected
