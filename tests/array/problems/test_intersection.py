import pytest

from kata.array.problems.intersection import intersect


class TestIntersect:
    @pytest.mark.parametrize(
        "a, b, expected",
        [
            ([], [], []),
            ([1], [], []),
            ([], [1], []),
            ([1], [2], []),
            ([1, 2], [2, 3], [2]),
            ([1, 2, 3, 4, 5], [0, 2, 4, 6, 8], [2, 4]),
        ],
    )
    def test(self, a: list[int], b: list[int], expected: list[int]) -> None:
        actual = intersect(a, b)
        assert actual == expected
