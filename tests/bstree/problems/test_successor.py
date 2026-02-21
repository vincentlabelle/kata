from kata.bstree.problems.successor import successor
from kata.btree.structures.bpnode import BPNode


class TestSuccessor:
    def test_when_direct_parent(self) -> None:
        two = BPNode(2)
        one = BPNode(1, left=two)
        assert successor(two) == one.value

    def test_when_indirect_parent(self) -> None:
        three = BPNode(3)
        one = BPNode(1, left=BPNode(2, right=three))
        assert successor(three) == one.value

    def test_when_none(self) -> None:
        three = BPNode(3)
        _ = BPNode(1, right=BPNode(2, right=three))
        assert successor(three) is None

    def test_when_direct_child(self) -> None:
        two = BPNode(2)
        one = BPNode(1, right=two)
        assert successor(one) == two.value

    def test_when_indirect_child(self) -> None:
        four = BPNode(4)
        one = BPNode(1, right=BPNode(2, left=BPNode(3, left=BPNode(4))))
        assert successor(one) == four.value
