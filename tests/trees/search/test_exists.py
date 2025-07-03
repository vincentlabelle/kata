import pytest

from kata.trees.bnode import BNode
from kata.trees.search.exists import exists


class TestExists:
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
        assert exists(node, value) is expected
