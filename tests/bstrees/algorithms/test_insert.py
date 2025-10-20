import pytest

from kata.bstrees.algorithms.insert import insert
from kata.btrees.structures.bnode import BNode


class TestInsert:
    @pytest.mark.parametrize(
        "node, value, expected",
        [
            (
                BNode(0),
                1,
                BNode(0, right=BNode(1)),
            ),
            (
                BNode(0),
                0,
                BNode(0, left=BNode(0)),
            ),
            (
                BNode(0),
                -1,
                BNode(0, left=BNode(-1)),
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
                -1,
                BNode(
                    0,
                    left=BNode(
                        -10,
                        left=BNode(-20),
                        right=BNode(-1),
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
                            right=BNode(
                                200,
                                right=BNode(250),
                            ),
                        ),
                    ),
                ),
            ),
        ],
    )
    def test(self, node: BNode[int], value: int, expected: BNode[int]) -> None:
        insert(node, value)
        assert node == expected
