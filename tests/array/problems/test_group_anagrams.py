import pytest

from kata.array.problems.group_anagrams import group_anagrams


class TestGroupAnagrams:
    @pytest.mark.parametrize(
        "array, expected",
        [
            ([], []),
            (["a"], ["a"]),
            (
                ["a", "b"],
                ["a", "b"],
            ),
            (
                ["listen", "bonus", "silent"],
                ["listen", "silent", "bonus"],
            ),
            (
                ["listen", "bonus", "silent"],
                ["listen", "silent", "bonus"],
            ),
            (
                ["listen", "evil", "silent", "vile"],
                ["listen", "silent", "evil", "vile"],
            ),
            (
                ["vile", "listen", "evil", "silent"],
                ["vile", "evil", "listen", "silent"],
            ),
            (
                ["vile", "listen", "bonus", "evil", "silent"],
                ["vile", "evil", "listen", "silent", "bonus"],
            ),
            (
                ["vile", "vile", "bonus", "evil", "silent"],
                ["vile", "vile", "evil", "bonus", "silent"],
            ),
        ],
    )
    def test(self, array: list[str], expected: list[str]) -> None:
        group_anagrams(array)
        assert array == expected
