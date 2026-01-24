import pytest

from kata.array.problems.one_away import one_away


class TestOneAway:
    @pytest.mark.parametrize(
        "one, two, expected",
        [
            ("", "", True),
            ("a", "a", True),
            ("abc", "abc", True),
            ("a", "b", True),
            ("abc", "dbc", True),
            ("abc", "adc", True),
            ("abc", "abd", True),
            ("abc", "ddc", False),
            ("abc", "dbd", False),
            ("abc", "add", False),
            ("", "ab", False),
            ("", "a", True),
            ("a", "", True),
            ("a", "ab", True),
            ("a", "ba", True),
            ("a", "bd", False),
            ("abc", "abcd", True),
            ("abc", "abdc", True),
            ("abc", "adbc", True),
            ("abc", "dabc", True),
            ("abc", "debc", False),
            ("abc", "daec", False),
            ("abc", "dabe", False),
        ],
    )
    def test(self, one: str, two: str, expected: bool) -> None:
        assert one_away(one, two) == expected
