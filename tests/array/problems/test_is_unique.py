import pytest

from kata.array.problems.is_unique import is_unique


class TestIsUnique:
    @pytest.mark.parametrize(
        "str_, expected",
        [
            ("", True),
            ("a", True),
            ("ab", True),
            ("aa", False),
            ("abc", True),
            ("aba", False),
        ],
    )
    def test(self, str_: str, expected: bool) -> None:
        assert is_unique(str_) == expected
