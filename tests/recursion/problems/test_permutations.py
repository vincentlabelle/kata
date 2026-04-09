import pytest

from kata.recursion.problems.permutations import permutations


class TestPermutations:
    @pytest.mark.parametrize(
        "s, expected",
        [
            ("", []),
            ("a", ["a"]),
            ("ab", ["ab", "ba"]),
            ("abc", ["cab", "acb", "abc", "cba", "bca", "bac"]),
        ],
    )
    def test(self, s: str, expected: list[str]) -> None:
        actual = permutations(s)
        assert len(actual) == len(expected)
        for e in expected:
            assert e in actual
