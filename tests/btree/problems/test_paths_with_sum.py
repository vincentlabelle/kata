import pytest

from kata.btree.problems.paths_with_sum import paths_with_sum
from kata.btree.structures.bnode import BNode


class TestPathsWithSum:
    @pytest.mark.parametrize(
        "node, target, expected",
        [
            (BNode(1), 0, 0),
            (BNode(1), 1, 1),
            (BNode(1, left=BNode(0)), 2, 0),
            (BNode(1, left=BNode(0)), 1, 2),
            (BNode(1, left=BNode(0)), 0, 1),
            (BNode(1, left=BNode(2)), 2, 1),
            (BNode(1, left=BNode(2), right=BNode(3)), 0, 0),
            (BNode(1, left=BNode(2), right=BNode(3)), 1, 1),
            (BNode(1, left=BNode(2), right=BNode(3)), 2, 1),
            (BNode(1, left=BNode(2), right=BNode(3)), 3, 2),
            (BNode(1, left=BNode(2), right=BNode(3)), 4, 1),
            (
                BNode(
                    1,
                    left=BNode(
                        2,
                        left=BNode(-1),
                        right=BNode(0),
                    ),
                    right=BNode(3),
                ),
                -1,
                1,
            ),
            (
                BNode(
                    1,
                    left=BNode(
                        2,
                        left=BNode(-1),
                        right=BNode(0),
                    ),
                    right=BNode(3),
                ),
                0,
                1,
            ),
            (
                BNode(
                    1,
                    left=BNode(
                        2,
                        left=BNode(-1),
                        right=BNode(0),
                    ),
                    right=BNode(3),
                ),
                2,
                3,
            ),
            (
                BNode(
                    1,
                    left=BNode(
                        2,
                        left=BNode(-1),
                        right=BNode(0),
                    ),
                    right=BNode(3),
                ),
                3,
                3,
            ),
            (
                BNode(
                    1,
                    left=BNode(
                        2,
                        left=BNode(-1),
                        right=BNode(0),
                    ),
                    right=BNode(3),
                ),
                4,
                1,
            ),
        ],
    )
    def test(self, node: BNode[int], target: int, expected: int) -> None:
        assert paths_with_sum(node, target) == expected
