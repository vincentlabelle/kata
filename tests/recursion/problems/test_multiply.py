import pytest

from kata.recursion.problems.multiply import multiply


class TestMultiply:
    @pytest.mark.parametrize(
        "a, b",
        [
            (3, 0),
            (3, 1),
            (3, 2),
            (3, 3),
            (3, 4),
            (3, 5),
            (0, 3),
            (1, 3),
            (2, 3),
            (4, 3),
            (5, 3),
        ],
    )
    def test_when_succeeds(self, a: int, b: int) -> None:
        assert multiply(a, b) == a * b

    @pytest.mark.parametrize("a, b", [(0, -1), (-1, 0)])
    def test_when_raises_value_error(self, a: int, b: int) -> None:
        with pytest.raises(ValueError):
            multiply(a, b)
