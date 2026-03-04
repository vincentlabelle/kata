import pytest

from kata.bit.problems.flip_bit import flip_bit


class TestFlipBit:
    @pytest.mark.parametrize(
        "value, expected",
        [
            (0, 1),
            (1, 2),
            (2, 2),
            (3, 3),
            (4, 2),
            (5, 3),
            (6, 3),
            (7, 4),
            (8, 2),
            (9, 2),
            (10, 3),
            (11, 4),
            (12, 3),
            (13, 4),
            (14, 4),
            (15, 5),
        ],
    )
    def test_when_succeeds(self, value: int, expected: int) -> None:
        assert flip_bit(value) == expected

    @pytest.mark.parametrize("value", [-1, -2])
    def test_when_raises_value_error(self, value: int) -> None:
        with pytest.raises(ValueError):
            flip_bit(value)
