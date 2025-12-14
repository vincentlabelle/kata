import pytest

from kata.array.problems.unique import search


class TestSearch:
    @pytest.mark.parametrize(
        "array, expected",
        [
            ([], None),
            (["a"], "a"),
            (["a", "b"], "a"),
            (["a", "a"], None),
            (["a", "b", "a"], "b"),
            (["m", "i", "n", "i", "m", "u", "m"], "n"),
        ],
    )
    def test(self, array: list[str], expected: str | None) -> None:
        assert search(array) == expected
