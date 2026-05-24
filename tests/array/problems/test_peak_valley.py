import pytest

from kata.array.problems.peak_valley import peak_valley


class TestPeakValley:
    @pytest.mark.parametrize(
        "array, expected",
        [
            ([], []),
            ([1], [1]),
            ([1, 2], [1, 2]),
            ([2, 1, 3], [2, 3, 1]),
            ([4, 1, 3, 2], [1, 4, 2, 3]),
            ([1, 5, 4, 2, 3], [1, 5, 2, 4, 3]),
            ([5, 3, 1, 2, 3], [3, 5, 1, 3, 2]),
        ],
    )
    def test(self, array: list[int], expected: list[int]) -> None:
        peak_valley(array)
        assert array == expected
