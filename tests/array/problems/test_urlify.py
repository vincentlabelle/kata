import pytest

from kata.array.problems.urlify import urlify


class TestUrlify:
    @pytest.mark.parametrize(
        "array, count, expected",
        [
            (
                [],
                0,
                [],
            ),
            (
                ["a"],
                1,
                ["a"],
            ),
            (
                [" ", "", ""],
                1,
                ["%", "2", "0"],
            ),
            (
                ["a", "b", "c"],
                3,
                ["a", "b", "c"],
            ),
            (
                ["a", "b", " ", "c", "d", " ", "e", "", "", "", ""],
                7,
                ["a", "b", "%", "2", "0", "c", "d", "%", "2", "0", "e"],
            ),
        ],
    )
    def test_when_succeeds(
        self,
        array: list[str],
        count: int,
        expected: list[str],
    ) -> None:
        urlify(array, count)
        assert array == expected

    @pytest.mark.parametrize(
        "array, count",
        [
            ([], -1),
            ([], 1),
            ([1], 2),
        ],
    )
    def test_when_raises_value_error(
        self,
        array: list[str],
        count: int,
    ) -> None:
        with pytest.raises(ValueError):
            urlify(array, count)
