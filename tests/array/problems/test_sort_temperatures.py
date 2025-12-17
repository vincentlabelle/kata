import pytest

from kata.array.problems.sort_temperatures import sort_temperatures


class TestSortTemperatures:
    @pytest.mark.parametrize(
        "array",
        [
            [],
            [970],
            [970, 980],
            [980, 970],
            [970, 975, 980, 985, 990],
            [990, 985, 980, 975, 970],
            [980, 975, 990, 985, 970],
        ],
    )
    def test(self, array: list[int]) -> None:
        assert sort_temperatures(array) == sorted(array)
