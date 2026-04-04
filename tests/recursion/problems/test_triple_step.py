import pytest

from kata.recursion.problems.triple_step import triple_step


class TestTripleStep:
    @pytest.mark.parametrize(
        "n, expected",
        [
            (-1, 0),
            (0, 0),
            (1, 1),
            (2, 2),
            (3, 4),
            (4, 7),
            (5, 13),
        ],
    )
    def test(self, n: int, expected: int) -> None:
        assert triple_step(n) == expected
