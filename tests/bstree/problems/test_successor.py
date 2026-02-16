from kata.bstree.problems.successor import successor
from kata.btree.structures.bpnode import BPNode


class TestSuccessor:
    def test_when_direct_parent(self) -> None:
        one, two = BPNode(1), BPNode(2)
        one.left, two.parent = two, one
        assert successor(two) == one.value

    def test_when_indirect_parent(self) -> None:
        one, two, three = BPNode(1), BPNode(2), BPNode(3)
        one.left, two.parent = two, one
        two.right, three.parent = three, two
        assert successor(three) == one.value

    def test_when_none(self) -> None:
        one, two, three = BPNode(1), BPNode(2), BPNode(3)
        one.right, two.parent = two, one
        two.right, three.parent = three, two
        assert successor(three) is None

    def test_when_direct_child(self) -> None:
        one, two = BPNode(1), BPNode(2)
        one.right, two.parent = two, one
        assert successor(one) == two.value

    def test_when_indirect_child(self) -> None:
        one, two, three, four = BPNode(1), BPNode(2), BPNode(3), BPNode(4)
        one.right, two.parent = two, one
        two.left, three.parent = three, two
        three.left, four.parent = four, three
        assert successor(one) == four.value
