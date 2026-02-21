from kata.btree.problems.first_common_ancestor import first_common_ancestor
from kata.btree.structures.bpnode import BPNode


class TestFirstCommonAncestor:
    def test_when_same(self) -> None:
        one = BPNode(1)
        assert first_common_ancestor(one, one) == one

    def test_when_direct(self) -> None:
        two = BPNode(2)
        one = BPNode(1, right=two)
        assert first_common_ancestor(one, two) == one
        assert first_common_ancestor(two, one) == one

    def test_when_indirect(self) -> None:
        three = BPNode(3)
        one = BPNode(1, right=BPNode(2, left=three))
        assert first_common_ancestor(one, three) == one
        assert first_common_ancestor(three, one) == one

    def test_when_subtree(self) -> None:
        three, four = BPNode(3), BPNode(4)
        one = BPNode(
            1,
            right=BPNode(
                2,
                left=three,
            ),
            left=four,
        )
        assert first_common_ancestor(three, four) == one
        assert first_common_ancestor(four, three) == one
