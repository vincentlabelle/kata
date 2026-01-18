import pytest

from kata.array.problems.compression import compression


class TestCompression:
    @pytest.mark.parametrize(
        "str_, expected",
        [
            ("", ""),
            ("a", "a"),
            ("aa", "aa"),
            ("ab", "ab"),
            ("aaa", "a3"),
            ("aab", "aab"),
            ("aaaa", "a4"),
            ("aaab", "aaab"),
            ("aaaaa", "a5"),
            ("aaaab", "a4b1"),
            ("aaabb", "a3b2"),
            ("aaabbcccc", "a3b2c4"),
            ("aaabbccccaa", "a3b2c4a2"),
        ],
    )
    def test(self, str_: str, expected: str) -> None:
        assert compression(str_) == expected
