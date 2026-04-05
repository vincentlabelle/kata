import pytest

from kata.recursion.problems.power_set import power_set


class TestPowerSet:
    @pytest.mark.parametrize(
        "set_, expected",
        [
            (
                set(),
                [set()],
            ),
            (
                {1},
                [set(), {1}],
            ),
            (
                {1, 2},
                [set(), {1}, {2}, {1, 2}],
            ),
            (
                {1, 2, 3},
                [set(), {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}],
            ),
        ],
    )
    def test(self, set_: set[int], expected: list[set[int]]) -> None:
        actual = power_set(set_)
        assert len(expected) == len(actual)
        for e in expected:
            assert e in actual
