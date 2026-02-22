from random import seed

import pytest

from kata.bstree.problems.random import random
from kata.btree.structures.bnode import BNode


class TestRandom:
    @pytest.mark.parametrize(
        "node, expected",
        [
            (
                BNode(1),
                [1],
            ),
            (
                BNode(
                    3,
                    left=BNode(0),
                    right=BNode(
                        6,
                        left=BNode(4, right=BNode(5)),
                        right=BNode(7),
                    ),
                ),
                [3, 6, 0, 4, 0, 5, 5, 5, 7],
            ),
        ],
    )
    def test(self, node: BNode[int], expected: list[int]) -> None:
        seed(1)
        for e in expected:
            assert random(node) == e
