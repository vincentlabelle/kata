import pytest

from kata.bit.problems.next_number import next_number


class TestNextNumber:
    @pytest.mark.parametrize(
        "value, expected",
        [
            (0b1, 0b10),
            (0b11, 0b101),
            (0b10, 0b100),
            (0b100, 0b1000),
            (0b110, 0b1001),
            (0b1100, 0b10001),
            (0b1110, 0b10011),
        ],
    )
    def test_when_succeeds(self, value: int, expected: int) -> None:
        assert next_number(value) == expected

    @pytest.mark.parametrize("value", [0, -1])
    def test_when_raises_value_error(self, value: int) -> None:
        with pytest.raises(ValueError):
            next_number(value)
