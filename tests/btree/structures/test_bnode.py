from typing import Any

import pytest

from kata.btree.structures.bnode import BNode


class TestBNodeEq:
    @pytest.fixture(
        params=[
            BNode(0),
            BNode(0, left=BNode(1)),
            BNode(0, right=BNode(1)),
            BNode(0, left=BNode(1), right=BNode(2)),
            BNode(
                0,
                left=BNode(1),
                right=BNode(1, left=BNode(2)),
            ),
        ]
    )
    def node(self, request: Any) -> BNode[int]:
        return request.param  # type: ignore[no-any-return]

    def test_when_equal(self, node: BNode[int]) -> None:
        other = BNode(
            node.value,
            left=node.left,
            right=node.right,
        )
        assert other == node

    def test_when_different_value(self, node: BNode[int]) -> None:
        other = BNode(
            node.value + 1,
            left=node.left,
            right=node.right,
        )
        assert other != node

    def test_when_different_left(self, node: BNode[int]) -> None:
        other = BNode(
            node.value,
            left=node.right or BNode(100),
            right=node.right,
        )
        assert other != node

    def test_when_different_right(self, node: BNode[int]) -> None:
        other = BNode(
            node.value,
            left=node.left,
            right=node.left or BNode(100),
        )
        assert other != node

    def test_when_different_type(self, node: BNode[int]) -> None:
        assert node != "a"


class TestBNodeStr:
    @pytest.mark.parametrize(
        "node, expected",
        [
            (BNode(0), "0"),
            (
                BNode(0, left=BNode(1)),
                f"0\n{BNode._TURN}1",
            ),
            (
                BNode(0, right=BNode(1)),
                f"0\n{BNode._TURN}1",
            ),
            (
                BNode(0, left=BNode(1), right=BNode(2)),
                f"0\n{BNode._SPLIT}1\n{BNode._TURN}2",
            ),
            (
                BNode(
                    0,
                    left=BNode(
                        1,
                        left=BNode(3),
                        right=BNode(
                            4,
                            left=BNode(
                                5,
                                left=BNode(
                                    7,
                                    right=BNode(9),
                                ),
                            ),
                            right=BNode(
                                6,
                                right=BNode(8),
                            ),
                        ),
                    ),
                    right=BNode(
                        2,
                        right=BNode(10),
                    ),
                ),
                (
                    "0\n"
                    + f"{BNode._SPLIT}1\n"
                    + f"{BNode._SPLIT_INDENT}{BNode._SPLIT}3\n"
                    + f"{BNode._SPLIT_INDENT}{BNode._TURN}4\n"
                    + f"{BNode._SPLIT_INDENT}{BNode._TURN_INDENT}{BNode._SPLIT}5\n"  # noqa: E501
                    + f"{BNode._SPLIT_INDENT}{BNode._TURN_INDENT}{BNode._SPLIT_INDENT}{BNode._TURN}7\n"  # noqa: E501
                    + f"{BNode._SPLIT_INDENT}{BNode._TURN_INDENT}{BNode._SPLIT_INDENT}{BNode._TURN_INDENT}{BNode._TURN}9\n"  # noqa: E501
                    + f"{BNode._SPLIT_INDENT}{BNode._TURN_INDENT}{BNode._TURN}6\n"  # noqa: E501
                    + f"{BNode._SPLIT_INDENT}{BNode._TURN_INDENT}{BNode._TURN_INDENT}{BNode._TURN}8\n"  # noqa: E501
                    + f"{BNode._TURN}2\n"
                    + f"{BNode._TURN_INDENT}{BNode._TURN}10"
                ),
            ),
        ],
    )
    def test(self, node: BNode[int], expected: str) -> None:
        assert str(node) == expected


class TestBNodeRepr:
    def test(self) -> None:
        node = BNode(0)
        expected = f"{node.__class__.__name__}(\n{node}\n)"
        assert repr(node) == expected
