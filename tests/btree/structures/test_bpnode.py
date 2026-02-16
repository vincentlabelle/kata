import pytest

from kata.btree.structures.bpnode import BPNode


@pytest.fixture(scope="function")
def node() -> BPNode[int]:
    return BPNode(0)


class TestBPNodeStr:
    def test(self, node: BPNode[int]) -> None:
        assert str(node) == str(id(node))


class TestBPNodeRepr:
    def test(self, node: BPNode[int]) -> None:
        expected = f"{node.__class__.__name__}({node})"
        assert repr(node) == expected
