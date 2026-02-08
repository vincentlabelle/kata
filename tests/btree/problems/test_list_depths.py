import pytest

from kata.btree.problems.list_depths import list_depths
from kata.btree.structures.bnode import BNode


class TestListDepths:
    @pytest.mark.parametrize(
        "node, expected",
        [
            (
                BNode(0),
                [[0]],
            ),
            (
                BNode(0, left=BNode(1)),
                [[0], [1]],
            ),
            (
                BNode(0, right=BNode(1)),
                [[0], [1]],
            ),
            (
                BNode(0, left=BNode(1), right=BNode(2)),
                [[0], [1, 2]],
            ),
            (
                BNode(0, left=BNode(1, left=BNode(2))),
                [[0], [1], [2]],
            ),
            (
                BNode(0, left=BNode(1, right=BNode(2))),
                [[0], [1], [2]],
            ),
            (
                BNode(0, left=BNode(1, left=BNode(3)), right=BNode(2)),
                [[0], [1, 2], [3]],
            ),
            (
                BNode(
                    0,
                    left=BNode(1, left=BNode(3)),
                    right=BNode(2, left=BNode(4)),
                ),
                [[0], [1, 2], [3, 4]],
            ),
            (
                BNode(
                    0,
                    left=BNode(1, left=BNode(3), right=BNode(4)),
                    right=BNode(2, left=BNode(5), right=BNode(6)),
                ),
                [[0], [1, 2], [3, 4, 5, 6]],
            ),
        ],
    )
    def test(self, node: BNode[int], expected: list[list[int]]) -> None:
        assert list_depths(node) == expected
