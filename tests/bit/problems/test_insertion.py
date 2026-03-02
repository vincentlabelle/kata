import pytest

from kata.bit.problems.insertion import insertion


class TestInsertion:
    @pytest.mark.parametrize(
        "n, m, i, j, expected",
        [
            (0, 0, 0, 0, 0),
            (2, 1, 0, 0, 3),
            (3, 1, 0, 0, 3),
            (3, 0, 0, 0, 2),
            (4, 2, 0, 1, 6),
            (7, 2, 0, 1, 6),
            (5, 1, 1, 1, 7),
            (7, 0, 1, 1, 5),
            (7, 2, 1, 2, 5),
        ],
    )
    def test_when_succeeds(
        self,
        n: int,
        m: int,
        i: int,
        j: int,
        expected: int,
    ) -> None:
        assert insertion(n, m, i=i, j=j) == expected

    @pytest.mark.parametrize(
        "i, j",
        [
            (-1, 0),
            (0, -1),
            (1, 0),
        ],
    )
    def test_when_raises_value_error(self, i: int, j: int) -> None:
        with pytest.raises(ValueError):
            insertion(200, 2, i=i, j=j)
