import pytest

from kata.trie.structures.tnode import TNode


@pytest.fixture(scope="function")
def node(map_: dict[str, TNode | None]) -> TNode:
    node = TNode()
    for key, value in map_.items():
        node[key] = value
    return node


@pytest.fixture(scope="function")
def map_() -> dict[str, TNode | None]:
    return {"a": None, "b": None, "c": TNode()}


class TestTNodeGetItem:
    def test_when_succeeds(
        self,
        node: TNode,
        map_: dict[str, TNode | None],
    ) -> None:
        for key, value in map_.items():
            assert node[key] == value

    def test_when_raises_key_error(self, node: TNode) -> None:
        with pytest.raises(KeyError):
            node["z"]


class TestTNodeSetItem:
    def test(self, node: TNode) -> None:
        key = "z"
        node[key] = None
        assert node[key] is None
        other = TNode()
        node[key] = other
        assert node[key] is other


class TestTNodeDelItem:
    def test_when_succeeds(
        self,
        node: TNode,
        map_: dict[str, TNode | None],
    ) -> None:
        for key in map_:
            del node[key]
            assert key not in node

    def test_when_raises_key_error(self, node: TNode) -> None:
        with pytest.raises(KeyError):
            del node["z"]


class TestTNodeLen:
    def test(self, node: TNode, map_: dict[str, TNode | None]) -> None:
        assert len(node) == len(map_)


class TestTNodeIter:
    def test(self, node: TNode, map_: dict[str, TNode | None]) -> None:
        assert tuple(iter(node)) == tuple(iter(map_))


class TestTNodeEq:
    def test_when_equal(
        self,
        node: TNode,
        map_: dict[str, TNode | None],
    ) -> None:
        other = TNode()
        for key, value in map_.items():
            other[key] = value
        assert other == node

    def test_when_different_map(
        self,
        node: TNode,
        map_: dict[str, TNode | None],
    ) -> None:
        other = TNode()
        for key in map_:
            other[key] = None
        assert other != node

    def test_when_different_type(self, node: TNode) -> None:
        assert node != "a"


class TestTNodeStr:
    def test(self, node: TNode, map_: dict[str, TNode | None]) -> None:
        assert str(node) == str(map_)


class TestTNodeRepr:
    def test(self, node: TNode) -> None:
        assert repr(node) == f"{node.__class__.__name__}({node})"
