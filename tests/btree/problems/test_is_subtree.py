import pytest

from kata.btree.problems.is_subtree import is_subtree
from kata.btree.structures.bnode import BNode


class TestIsSubtree:
    @pytest.mark.parametrize(
        "one, two, expected",
        [
            (BNode(1), BNode(1), True),
            (BNode(1), BNode(0), False),
            (
                BNode(
                    1,
                    left=BNode(0),
                    right=BNode(
                        2,
                        left=BNode(3),
                        right=BNode(4),
                    ),
                ),
                BNode(4),
                True,
            ),
            (
                BNode(
                    1,
                    left=BNode(0),
                    right=BNode(
                        2,
                        left=BNode(3, right=BNode(5)),
                        right=BNode(4),
                    ),
                ),
                BNode(3, right=BNode(5)),
                True,
            ),
            (
                BNode(
                    1,
                    left=BNode(0),
                    right=BNode(
                        2,
                        left=BNode(3, right=BNode(5)),
                        right=BNode(4),
                    ),
                ),
                BNode(
                    2,
                    left=BNode(3, right=BNode(5)),
                    right=BNode(4),
                ),
                True,
            ),
            (
                BNode(
                    1,
                    left=BNode(0),
                    right=BNode(
                        2,
                        left=BNode(3, right=BNode(5)),
                        right=BNode(4),
                    ),
                ),
                BNode(
                    1,
                    left=BNode(0),
                    right=BNode(
                        2,
                        left=BNode(3, right=BNode(5)),
                        right=BNode(4),
                    ),
                ),
                True,
            ),
            (
                BNode(
                    1,
                    left=BNode(0),
                    right=BNode(
                        2,
                        left=BNode(3, right=BNode(5)),
                        right=BNode(4),
                    ),
                ),
                BNode(3),
                False,
            ),
            (
                BNode(
                    1,
                    left=BNode(0),
                    right=BNode(
                        2,
                        left=BNode(3, right=BNode(5)),
                        right=BNode(4),
                    ),
                ),
                BNode(
                    2,
                    left=BNode(3, right=BNode(6)),
                    right=BNode(4),
                ),
                False,
            ),
        ],
    )
    def test(
        self,
        one: BNode[int],
        two: BNode[int],
        expected: bool,
    ) -> None:
        assert is_subtree(one, two) == expected
