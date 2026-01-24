import pytest

from kata.linked.problems.remove_duplicates import remove_duplicates
from kata.linked.structures.snode import SNode


class TestRemoveDuplicates:
    @pytest.mark.parametrize(
        "head, expected",
        [
            (SNode(0), SNode(0)),
            (SNode(0, SNode(1)), SNode(0, SNode(1))),
            (SNode(0, SNode(0)), SNode(0)),
            (SNode(0, SNode(1, SNode(2))), SNode(0, SNode(1, SNode(2)))),
            (SNode(0, SNode(1, SNode(0))), SNode(0, SNode(1))),
            (SNode(0, SNode(0, SNode(2))), SNode(0, SNode(2))),
            (SNode(0, SNode(1, SNode(1))), SNode(0, SNode(1))),
            (SNode(0, SNode(0, SNode(0))), SNode(0)),
        ],
    )
    def test(self, head: SNode[int], expected: SNode[int]) -> None:
        remove_duplicates(head)
        assert head == expected
