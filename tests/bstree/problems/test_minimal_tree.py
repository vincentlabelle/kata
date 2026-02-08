import pytest

from kata.bstree.problems.minimal_tree import minimal_tree
from kata.btree.structures.bnode import BNode


class TestMinimalTree:
    @pytest.mark.parametrize(
        "array, expected",
        [
            (
                [],
                None,
            ),
            (
                [1],
                BNode(1),
            ),
            (
                [1, 2],
                BNode(1, right=BNode(2)),
            ),
            (
                [1, 2, 3],
                BNode(2, left=BNode(1), right=BNode(3)),
            ),
            (
                [1, 2, 3, 4],
                BNode(2, left=BNode(1), right=BNode(3, right=BNode(4))),
            ),
            (
                [1, 2, 3, 4, 5],
                BNode(
                    3,
                    left=BNode(1, right=BNode(2)),
                    right=BNode(4, right=BNode(5)),
                ),
            ),
            (
                [1, 2, 3, 4, 5, 6],
                BNode(
                    3,
                    left=BNode(1, right=BNode(2)),
                    right=BNode(5, left=BNode(4), right=BNode(6)),
                ),
            ),
        ],
    )
    def test(self, array: list[int], expected: BNode[int] | None) -> None:
        assert minimal_tree(array) == expected
