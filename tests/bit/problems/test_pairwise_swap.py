import pytest

from kata.bit.problems.pairwise_swap import pairwise_swap


class TestPairwiseSwap:
    @pytest.mark.parametrize(
        "value, expected",
        [
            (0, 0),
            (1, 2),
            (0xAAAAAAAA, 0x55555555),
            (0x55555555, 0xAAAAAAAA),
        ],
    )
    def test_when_succeeds(self, value: int, expected: int) -> None:
        assert pairwise_swap(value) == expected

    @pytest.mark.parametrize("value", [-1, 1 << 32])
    def test_when_raises_value_error(self, value: int) -> None:
        with pytest.raises(ValueError):
            pairwise_swap(value)
