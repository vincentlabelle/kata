import pytest

from kata.array.problems.sumswap import swap


class TestSwap:
    @pytest.mark.parametrize(
        "one, two, expected",
        [
            ([], [], None),
            ([1], [], None),
            ([], [1], None),
            ([1], [1], None),
            ([1], [3], None),
            ([1, 4], [3, 2], None),
            ([1, 2], [3, 5], None),
            ([1, 2], [3, 4], (0, 0)),
            ([5, 3, 2, 9, 1], [1, 12, 5], (2, 0)),
        ],
    )
    def test(
        self,
        one: list[int],
        two: list[int],
        expected: tuple[int, int] | None,
    ) -> None:
        assert swap(one, two) == expected
