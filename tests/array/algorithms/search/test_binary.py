import pytest

from kata.array.algorithms.search.binary import search


class TestSearch:
    @pytest.mark.parametrize(
        "array, value, expected",
        [
            ([], 0, -1),
            ([0], 1, -1),
            ([1], 1, 0),
            ([1, 2, 3, 4, 5], 1, 0),
            ([1, 2, 3, 4, 5], 2, 1),
            ([1, 2, 3, 4, 5], 3, 2),
            ([1, 2, 3, 4, 5], 4, 3),
            ([1, 2, 3, 4, 5], 5, 4),
            ([1, 2, 3, 4, 5, 6], 1, 0),
            ([1, 2, 3, 4, 5, 6], 2, 1),
            ([1, 2, 3, 4, 5, 6], 3, 2),
            ([1, 2, 3, 4, 5, 6], 4, 3),
            ([1, 2, 3, 4, 5, 6], 5, 4),
            ([1, 2, 3, 4, 5, 6], 6, 5),
        ],
    )
    def test(self, array: list[int], value: int, expected: int) -> None:
        assert search(array, value) == expected
