import pytest

from kata.bit.problems.binary_to_string import binary_to_string


class TestBinaryToString:
    @pytest.mark.parametrize(
        "value, expected",
        [
            (-0.25, "ERROR"),
            (0.0, "ERROR"),
            (0.1, "ERROR"),
            (1.0, "ERROR"),
            (0.25, "0.01"),
            (0.5, "0.1"),
            (0.625, "0.101"),
            (0.75, "0.11"),
            (0.875, "0.111"),
        ],
    )
    def test(self, value: float, expected: str) -> None:
        assert binary_to_string(value) == expected
