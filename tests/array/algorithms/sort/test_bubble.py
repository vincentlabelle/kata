import pytest

from kata.array.algorithms.sort.bubble import sort


class TestSort:
    @pytest.mark.parametrize(
        "array",
        [
            [],
            [1],
            [1, 2],
            [2, 1],
            [1, 2, 3, 4, 5],
            [5, 4, 3, 2, 1],
            [3, 2, 5, 4, 1],
        ],
    )
    def test(self, array: list[int]) -> None:
        expected = sorted(array)
        sort(array)
        assert array == expected
