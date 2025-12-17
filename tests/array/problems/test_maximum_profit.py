import pytest

from kata.array.problems.maximum_profit import maximum_profit


class TestMaximumProfit:
    @pytest.mark.parametrize(
        "array, expected",
        [
            ([], 0),
            ([1], 0),
            ([1, 1], 0),
            ([2, 1], 0),
            ([1, 2], 1),
            ([1, 1, 1], 0),
            ([3, 2, 1], 0),
            ([1, 2, 3], 2),
            ([1, 3, 2], 2),
            ([2, 1, 3], 2),
            ([10, 7, 5, 8, 7, 11, 2, 6], 6),
            ([10, 7, 5, 8, 7, 11, 2, 6, 20], 18),
        ],
    )
    def test(self, array: list[int], expected: int) -> None:
        assert maximum_profit(array) == expected
