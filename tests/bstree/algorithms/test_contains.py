import pytest

from kata.bstree.algorithms.contains import contains
from kata.btree.structures.bnode import BNode


class TestContains:
    @pytest.mark.parametrize(
        "node, value, expected",
        [
            (BNode(0), -1, False),
            (BNode(0), 0, True),
            (BNode(0), 1, False),
            (BNode(0, left=BNode(-1)), -2, False),
            (BNode(0, left=BNode(-1)), -1, True),
            (BNode(0, left=BNode(-1)), 0, True),
            (BNode(0, left=BNode(-1)), 1, False),
            (BNode(0, right=BNode(1)), -1, False),
            (BNode(0, right=BNode(1)), 0, True),
            (BNode(0, right=BNode(1)), 1, True),
            (BNode(0, right=BNode(1)), 2, False),
            (BNode(0, left=BNode(-1), right=BNode(1)), -2, False),
            (BNode(0, left=BNode(-1), right=BNode(1)), -1, True),
            (BNode(0, left=BNode(-1), right=BNode(1)), 0, True),
            (BNode(0, left=BNode(-1), right=BNode(1)), 1, True),
            (BNode(0, left=BNode(-1), right=BNode(1)), 2, False),
            (
                BNode(
                    0,
                    left=BNode(
                        -10,
                        left=BNode(-20),
                    ),
                    right=BNode(
                        100,
                        left=BNode(50),
                        right=BNode(
                            150,
                            right=BNode(200),
                        ),
                    ),
                ),
                -10,
                True,
            ),
            (
                BNode(
                    0,
                    left=BNode(
                        -10,
                        left=BNode(-20),
                    ),
                    right=BNode(
                        100,
                        left=BNode(50),
                        right=BNode(
                            150,
                            right=BNode(200),
                        ),
                    ),
                ),
                200,
                True,
            ),
            (
                BNode(
                    0,
                    left=BNode(
                        -10,
                        left=BNode(-20),
                    ),
                    right=BNode(
                        100,
                        left=BNode(50),
                        right=BNode(
                            150,
                            right=BNode(200),
                        ),
                    ),
                ),
                250,
                False,
            ),
        ],
    )
    def test(self, node: BNode[int], value: int, expected: bool) -> None:
        assert contains(node, value) is expected
