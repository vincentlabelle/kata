import pytest

from kata.recursion.problems.queens import queens


class TestQueens:
    @pytest.mark.parametrize(
        "n, expected",
        [
            (-1, []),
            (0, []),
            (1, [[0]]),
            (2, []),
            (3, []),
            (4, [[1, 3, 0, 2], [2, 0, 3, 1]]),
        ],
    )
    def test(self, n: int, expected: list[list[int]]) -> None:
        assert queens(n) == expected
