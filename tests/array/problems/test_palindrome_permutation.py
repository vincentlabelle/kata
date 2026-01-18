import pytest

from kata.array.problems.palindrome_permutation import palindrome_permutation


class TestPalindromePermutation:
    @pytest.mark.parametrize(
        "str_, expected",
        [
            ("", True),
            (" ", True),
            ("a", True),
            ("A", True),
            ("a ", True),
            ("aa", True),
            ("aA", True),
            ("ab", False),
            ("a a", True),
            ("Zbz", True),
            ("abA", True),
            ("aab", True),
            ("acb", False),
            ("ac cd", False),
            ("ac ca", True),
            ("ca cao", True),
        ],
    )
    def test(self, str_: str, expected: bool) -> None:
        assert palindrome_permutation(str_) == expected
