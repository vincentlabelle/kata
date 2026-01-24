import pytest

from kata.linked.problems.remove_preserve import remove_preserve
from kata.linked.structures.snode import SNode


class TestRemovePreserve:
    @pytest.fixture(scope="function")
    def linked(self) -> SNode[int]:
        return SNode(0, next_=SNode(1, next_=SNode(2)))

    @pytest.mark.parametrize(
        "index, expected",
        [
            (0, SNode(1, next_=SNode(2))),
            (1, SNode(0, next_=SNode(2))),
            (2, SNode(0, next_=SNode(1, next_=SNode(2)))),
        ],
    )
    def test(
        self,
        linked: SNode[int],
        index: int,
        expected: SNode[int],
    ) -> None:
        node = self._traverse(linked, index)
        remove_preserve(node)
        assert linked == expected

    def _traverse(self, linked: SNode[int] | None, index: int) -> SNode[int]:
        node, i = linked, 0
        while node is not None:
            if i == index:
                return node
            node, i = node.next, i + 1
        assert False
