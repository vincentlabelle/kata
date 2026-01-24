import pytest

from kata.array.problems.string_rotation import string_rotation


class TestStringRotation:
    @pytest.mark.parametrize(
        "one, two, expected",
        [
            ("", "", True),
            ("", "a", False),
            ("a", "", False),
            ("a", "a", True),
            ("ab", "ab", True),
            ("ab", "ba", True),
            ("ac", "ba", False),
            ("ca", "ba", False),
            ("abc", "abc", True),
            ("abc", "bca", True),
            ("abc", "cab", True),
            ("abc", "acb", False),
            ("abc", "cba", False),
        ],
    )
    def test(self, one: str, two: str, expected: bool) -> None:
        assert string_rotation(one, two) == expected
