import pytest

from kata.trees.binary.breadth import traverse
from kata.trees.bnode import BNode


class TestTraverse:
    @pytest.mark.parametrize(
        "node, expected",
        [
            (BNode(0), [0]),
            (
                BNode(
                    0,
                    left=BNode(1),
                ),
                [0, 1],
            ),
            (
                BNode(
                    0,
                    right=BNode(1),
                ),
                [0, 1],
            ),
            (
                BNode(
                    0,
                    left=BNode(1),
                    right=BNode(2),
                ),
                [0, 1, 2],
            ),
            (
                BNode(
                    0,
                    left=BNode(
                        1,
                        left=BNode(3),
                    ),
                    right=BNode(2),
                ),
                [0, 1, 2, 3],
            ),
            (
                BNode(
                    0,
                    left=BNode(
                        1,
                        left=BNode(3),
                        right=BNode(4),
                    ),
                    right=BNode(
                        2,
                        left=BNode(5),
                        right=BNode(
                            6,
                            right=BNode(7),
                        ),
                    ),
                ),
                [0, 1, 2, 3, 4, 5, 6, 7],
            ),
        ],
    )
    def test(self, node: BNode[int], expected: list[int]) -> None:
        assert traverse(node) == expected
