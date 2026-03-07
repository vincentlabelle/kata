import pytest

from kata.bit.problems.conversion import conversion


class TestConversion:
    @pytest.mark.parametrize(
        "one, two, expected",
        [
            (0, 0, 0),
            (15, 15, 0),
            (15, 14, 1),
            (15, 29, 2),
            (15, 16, 5),
        ],
    )
    def test_when_succeeds(self, one: int, two: int, expected: int) -> None:
        assert conversion(one, two) == expected

    @pytest.mark.parametrize(
        "one, two",
        [
            (-15, -15),
            (-15, 15),
            (15, -15),
        ],
    )
    def test_when_raises_value_error(self, one: int, two: int) -> None:
        with pytest.raises(ValueError):
            conversion(one, two)
