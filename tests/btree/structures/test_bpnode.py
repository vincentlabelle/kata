import pytest

from kata.btree.structures.bpnode import BPNode


@pytest.fixture(scope="function")
def node(left: BPNode[int], right: BPNode[int]) -> BPNode[int]:
    return BPNode(0, left=left, right=right)


@pytest.fixture(scope="function")
def left() -> BPNode[int]:
    return BPNode(1)


@pytest.fixture(scope="function")
def right() -> BPNode[int]:
    return BPNode(2)


class TestBpNodeParent:
    def test(
        self,
        node: BPNode[int],
        left: BPNode[int],
        right: BPNode[int],
    ) -> None:
        assert left.parent is node
        assert right.parent is node


class TestBpNodeLeft:
    def test_get(self, node: BPNode[int], left: BPNode[int]) -> None:
        assert node.left is left

    def test_set_when_none(self, right: BPNode[int]) -> None:
        other = BPNode(3)
        right.left = other
        assert right.left is other
        assert other.parent is right

    def test_set_when_node(self, node: BPNode[int], left: BPNode[int]) -> None:
        other = BPNode(3)
        previous = BPNode(4, left=other)
        node.left = other
        assert node.left is other
        assert other.parent is node
        assert left.parent is None
        assert previous.left is None

    def test_unset(self, node: BPNode[int], left: BPNode[int]) -> None:
        node.left = None
        assert node.left is None
        assert left.parent is None


class TestBpNodeRight:
    def test_get(self, node: BPNode[int], right: BPNode[int]) -> None:
        assert node.right is right

    def test_set_when_none(self, left: BPNode[int]) -> None:
        other = BPNode(3)
        left.right = other
        assert left.right is other
        assert other.parent is left

    def test_set_when_node(self, node: BPNode[int], right: BPNode[int]) -> None:
        other = BPNode(3)
        previous = BPNode(4, left=other)
        node.right = other
        assert node.right is other
        assert other.parent is node
        assert right.parent is None
        assert previous.left is None

    def test_unset(self, node: BPNode[int], right: BPNode[int]) -> None:
        node.right = None
        assert node.right is None
        assert right.parent is None


class TestBPNodeStr:
    def test(self, node: BPNode[int]) -> None:
        assert str(node) == str(id(node))


class TestBPNodeRepr:
    def test(self, node: BPNode[int]) -> None:
        expected = f"{node.__class__.__name__}({node})"
        assert repr(node) == expected
