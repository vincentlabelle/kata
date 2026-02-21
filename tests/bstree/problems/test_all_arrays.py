import pytest

from kata.bstree.problems.all_arrays import all_arrays
from kata.btree.structures.bnode import BNode


class TestAllArrays:
    @pytest.mark.parametrize(
        "node, expected",
        [
            (
                BNode(0),
                [[0]],
            ),
            (
                BNode(1, left=BNode(0)),
                [[1, 0]],
            ),
            (
                BNode(2, left=BNode(0, right=BNode(1))),
                [[2, 0, 1]],
            ),
            (
                BNode(1, left=BNode(0), right=BNode(2)),
                [[1, 0, 2], [1, 2, 0]],
            ),
            (
                BNode(
                    2,
                    left=BNode(1, left=BNode(0)),
                    right=BNode(3),
                ),
                [[2, 1, 3, 0], [2, 1, 0, 3], [2, 3, 1, 0]],
            ),
            (
                BNode(
                    3,
                    left=BNode(1, left=BNode(0), right=BNode(2)),
                    right=BNode(4),
                ),
                [
                    [3, 1, 4, 0, 2],
                    [3, 1, 4, 2, 0],
                    [3, 1, 0, 4, 2],
                    [3, 1, 0, 2, 4],
                    [3, 1, 2, 4, 0],
                    [3, 1, 2, 0, 4],
                    [3, 4, 1, 0, 2],
                    [3, 4, 1, 2, 0],
                ],
            ),
        ],
    )
    def test(self, node: BNode[int], expected: list[list[int]]) -> None:
        assert all_arrays(node) == expected
