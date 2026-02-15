import pytest

from kata.btree.problems.is_balanced import is_balanced
from kata.btree.structures.bnode import BNode


class TestIsBalanced:
    @pytest.mark.parametrize(
        "node, expected",
        [
            (
                BNode(0),
                True,
            ),
            (
                BNode(0, left=BNode(1)),
                True,
            ),
            (
                BNode(0, right=BNode(1)),
                True,
            ),
            (
                BNode(0, left=BNode(1), right=BNode(1)),
                True,
            ),
            (
                BNode(
                    0,
                    left=BNode(1, right=BNode(2)),
                    right=BNode(1),
                ),
                True,
            ),
            (
                BNode(
                    0,
                    left=BNode(
                        1,
                        right=BNode(3, left=BNode(5)),
                    ),
                    right=BNode(2, left=BNode(4)),
                ),
                False,
            ),
            (
                BNode(
                    0,
                    left=BNode(2, left=BNode(4)),
                    right=BNode(
                        1,
                        right=BNode(3, left=BNode(5)),
                    ),
                ),
                False,
            ),
            (
                BNode(
                    0,
                    left=BNode(2),
                    right=BNode(
                        1,
                        left=BNode(3),
                        right=BNode(4, left=BNode(5)),
                    ),
                ),
                False,
            ),
            (
                BNode(
                    0,
                    left=BNode(2, right=BNode(6)),
                    right=BNode(
                        1,
                        left=BNode(3),
                        right=BNode(4, left=BNode(5)),
                    ),
                ),
                True,
            ),
        ],
    )
    def test(self, node: BNode[int], expected: bool) -> None:
        assert is_balanced(node) == expected
