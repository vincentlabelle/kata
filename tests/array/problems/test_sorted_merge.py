import pytest

from kata.array.problems.sorted_merge import sorted_merge


class TestSortedMerge:
    @pytest.mark.parametrize(
        "one, two, expected",
        [
            ([], [], []),
            ([1], [], [1]),
            ([1], [2], [2]),
            ([1, 2], [3, 4], [3, 4]),
            ([1, -1], [2], [1, 2]),
            ([2, -1], [1], [1, 2]),
            ([1, 2, -1, -1], [3, 4], [1, 2, 3, 4]),
            ([2, 4, -1, -1], [1, 3], [1, 2, 3, 4]),
            ([2, 4, 5, -1, -1], [1, 3], [1, 2, 3, 4, 5]),
        ],
    )
    def test_when_succeeds(
        self,
        one: list[int],
        two: list[int],
        expected: list[int],
    ) -> None:
        sorted_merge(one, two)
        assert one == expected

    @pytest.mark.parametrize(
        "one, two",
        [
            ([], [1]),
            ([1], [2, 3]),
        ],
    )
    def test_when_raises_value_error(
        self,
        one: list[int],
        two: list[int],
    ) -> None:
        with pytest.raises(ValueError):
            sorted_merge(one, two)
