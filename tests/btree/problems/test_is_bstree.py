import pytest

from kata.btree.problems.is_bstree import is_bstree
from kata.btree.structures.bnode import BNode


class TestIsBstree:
    @pytest.mark.parametrize(
        "node, expected",
        [
            (
                BNode(0),
                True,
            ),
            (
                BNode(2, left=BNode(1)),
                True,
            ),
            (
                BNode(2, right=BNode(3)),
                True,
            ),
            (
                BNode(2, left=BNode(1), right=BNode(3)),
                True,
            ),
            (
                BNode(2, left=BNode(2), right=BNode(3)),
                True,
            ),
            (
                BNode(
                    2,
                    left=BNode(1, left=BNode(2)),
                    right=BNode(3),
                ),
                False,
            ),
            (
                BNode(
                    2,
                    left=BNode(1),
                    right=BNode(4, right=BNode(3)),
                ),
                False,
            ),
            (
                BNode(
                    10,
                    left=BNode(1),
                    right=BNode(
                        20,
                        left=BNode(10, right=BNode(15)),
                        right=BNode(30),
                    ),
                ),
                False,
            ),
            (
                BNode(
                    10,
                    left=BNode(1),
                    right=BNode(
                        20,
                        left=BNode(11, right=BNode(15)),
                        right=BNode(30),
                    ),
                ),
                True,
            ),
        ],
    )
    def test(self, node: BNode[int], expected: bool) -> None:
        assert is_bstree(node) == expected
