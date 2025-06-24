from typing import Any

import pytest

from kata.linked.snode import SNode


class TestSNodeEq:
    @pytest.fixture(
        params=[
            SNode(0),
            SNode(1, SNode(2, SNode(3))),
        ],
    )
    def node(self, request: Any) -> SNode[int]:
        return request.param  # type: ignore[no-any-return]

    def test_when_equal(self, node: SNode[int]) -> None:
        other = SNode(node.value, node.next)
        assert other == node

    def test_when_different_value(self, node: SNode[int]) -> None:
        other = SNode(node.value + 1, node.next)
        assert other != node

    def test_when_different_next(self, node: SNode[int]) -> None:
        next_ = SNode(100)
        other = SNode(node.value, next_)
        assert other != node

    def test_when_different_type(self, node: SNode[int]) -> None:
        assert node != "a"


class TestSNodeStr:
    @pytest.mark.parametrize(
        "node, expected",
        [
            (SNode(0), "0"),
            (SNode(0, SNode(1)), "0->1"),
            (SNode(0, SNode(1, SNode(2))), "0->1->2"),
        ],
    )
    def test(self, node: SNode[int], expected: str) -> None:
        assert str(node) == expected


class TestSNodeRepr:
    def test(self) -> None:
        node = SNode(0)
        assert repr(node) == f"{node.__class__.__name__}({node})"
