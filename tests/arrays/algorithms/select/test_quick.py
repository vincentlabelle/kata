import pytest

from kata.arrays.algorithms.select.quick import select


class TestSelect:
    @pytest.mark.parametrize(
        "array, position",
        [
            ([1], 0),
            ([1, 2], 0),
            ([1, 2], 1),
            ([2, 1], 0),
            ([2, 1], 1),
            ([1, 2, 3, 4, 5], 0),
            ([1, 2, 3, 4, 5], 2),
            ([1, 2, 3, 4, 5], 4),
            ([5, 4, 3, 2, 1], 0),
            ([5, 4, 3, 2, 1], 2),
            ([5, 4, 3, 2, 1], 4),
            ([3, 2, 5, 4, 1], 0),
            ([3, 2, 5, 4, 1], 2),
            ([3, 2, 5, 4, 1], 4),
        ],
    )
    def test_when_succeeds(self, array: list[int], position: int) -> None:
        expected = sorted(array)[position]
        actual = select(array, position)
        assert actual == expected

    @pytest.mark.parametrize(
        "array, position",
        [
            ([], 0),
            ([1], -1),
            ([1], 1),
            ([1, 2], -1),
            ([1, 2], 2),
        ],
    )
    def test_when_raises_value_error(
        self,
        array: list[int],
        position: int,
    ) -> None:
        with pytest.raises(ValueError):
            select(array, position)
