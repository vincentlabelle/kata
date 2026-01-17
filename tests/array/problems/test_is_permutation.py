import pytest

from kata.array.problems.is_permutation import is_permutation


class TestIsPermutation:
    @pytest.mark.parametrize(
        "one, two, expected",
        [
            ("", "", True),
            ("a", "a", True),
            ("ab", "ab", True),
            ("ab", "ba", True),
            ("aa", "aa", True),
            ("aa", "ac", False),
            ("aa", "ca", False),
            ("aba", "aba", True),
            ("", "a", False),
        ],
    )
    def test(self, one: str, two: str, expected: bool) -> None:
        assert is_permutation(one, two) == expected
