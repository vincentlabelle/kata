import pytest

from kata.array.problems.consecutive import get_longest


class TestGetLongest:
    @pytest.mark.parametrize(
        "array, expected",
        [
            ([], 0),
            ([1], 1),
            ([1, 2], 2),
            ([2, 1], 2),
            ([2, 4], 1),
            ([2, 2], 1),
            ([1, 2, 3, 4, 5], 5),
            ([1, 3, 5, 7, 9], 1),
            ([10, 5, 12, 3, 55, 30, 4, 11, 2], 4),
        ],
    )
    def test(self, array: list[int], expected: int) -> None:
        assert get_longest(array) == expected
