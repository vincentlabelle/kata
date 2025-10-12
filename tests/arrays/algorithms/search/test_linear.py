import pytest

from kata.arrays.algorithms.search.linear import search


class TestSearch:
    @pytest.mark.parametrize(
        "array, value, expected",
        [
            ([], 0, -1),
            ([0], 1, -1),
            ([1], 1, 0),
            ([2, 1, 3], 1, 1),
        ],
    )
    def test(self, array: list[int], value: int, expected: int) -> None:
        assert search(array, value) == expected
