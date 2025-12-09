import pytest

from kata.recursion.problems.uniquepaths import solve


class TestSolve:
    @pytest.mark.parametrize(
        "rows, columns, expected",
        [
            (-1, -1, 0),
            (0, -1, 0),
            (-1, 0, 0),
            (0, 0, 0),
            (1, 0, 0),
            (0, 1, 0),
            (1, 1, 0),
            (1, 2, 1),
            (2, 1, 1),
            (2, 2, 2),
            (2, 3, 3),
            (3, 2, 3),
            (3, 3, 6),
        ],
    )
    def test(self, rows: int, columns: int, expected: int) -> None:
        assert solve(rows, columns) == expected
