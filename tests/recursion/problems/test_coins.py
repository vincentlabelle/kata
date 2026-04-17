import pytest

from kata.recursion.problems.coins import coins


class TestCoins:
    @pytest.mark.parametrize(
        "total, expected",
        [
            (-1, 0),
            (0, 0),
            (1, 1),
            (4, 1),
            (9, 2),
            (10, 4),
            (16, 6),
            (20, 9),
            (25, 13),
        ],
    )
    def test(self, total: int, expected: int) -> None:
        assert coins(total) == expected
