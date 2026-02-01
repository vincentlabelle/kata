from kata.linked.problems.loop import loop
from kata.linked.structures.snode import SNode


class TestLoop:
    def test_when_direct_loop_at_head(self) -> None:
        loop_ = SNode(0)
        loop_.next = loop_
        assert loop(loop_) is loop_

    def test_when_direct_loop(self) -> None:
        loop_ = SNode(0)
        loop_.next = loop_
        head = SNode(1, loop_)
        assert loop(head) is loop_

    def test_when_indirect_loop_at_head(self) -> None:
        loop_ = SNode(0)
        loop_.next = SNode(1)
        loop_.next.next = loop_
        assert loop(loop_) is loop_

    def test_when_indirect_loop(self) -> None:
        loop_ = SNode(0)
        loop_.next = SNode(1)
        loop_.next.next = loop_
        head = SNode(2, SNode(3, loop_))
        assert loop(head) is loop_

    def test_when_no_loop(self) -> None:
        head = SNode(0, SNode(1, SNode(0)))
        assert loop(head) is None
