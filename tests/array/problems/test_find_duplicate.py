import pytest

from kata.array.problems.find_duplicate import find_duplicate


class TestFindDuplicate:
    @pytest.mark.parametrize(
        "array, expected",
        [
            ([], None),
            (["a"], None),
            (["a", "b"], None),
            (["a", "a"], "a"),
            (["a", "b", "a"], "a"),
            (["a", "b", "c", "d", "c"], "c"),
            (["a", "b", "c", "d", "c", "a"], "c"),
        ],
    )
    def test(self, array: list[str], expected: str | None) -> None:
        assert find_duplicate(array) == expected
