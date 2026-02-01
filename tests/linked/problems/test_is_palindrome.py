import pytest

from kata.linked.problems.is_palindrome import is_palindrome
from kata.linked.structures.snode import SNode


class TestIsPalindrome:
    @pytest.mark.parametrize(
        "head, expected",
        [
            (SNode("a"), True),
            (SNode("a", SNode("a")), True),
            (SNode("a", SNode("b")), False),
            (SNode("a", SNode("a", SNode("a"))), True),
            (SNode("a", SNode("b", SNode("a"))), True),
            (SNode("a", SNode("b", SNode("c"))), False),
            (SNode("a", SNode("a", SNode("b"))), False),
            (SNode("a", SNode("a", SNode("a", SNode("a")))), True),
            (SNode("a", SNode("b", SNode("b", SNode("a")))), True),
            (SNode("a", SNode("b", SNode("c", SNode("a")))), False),
            (SNode("a", SNode("b", SNode("b", SNode("c")))), False),
        ],
    )
    def test(self, head: SNode[str], expected: bool) -> None:
        assert is_palindrome(head) == expected
