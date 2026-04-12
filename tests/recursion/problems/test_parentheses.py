import pytest

from kata.recursion.problems.parentheses import parentheses


class TestParentheses:
    @pytest.mark.parametrize(
        "n, expected",
        [
            (-1, []),
            (0, []),
            (1, ["()"]),
            (2, ["(())", "()()"]),
            (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
        ],
    )
    def test(self, n: int, expected: list[str]) -> None:
        assert parentheses(n) == expected
