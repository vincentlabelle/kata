import pytest

from kata.recursion.problems.magic_index import magic_index


class TestMagicIndex:
    @pytest.mark.parametrize(
        "array, expected",
        [
            ([], -1),
            ([1], -1),
            ([0], 0),
            ([1, 2], -1),
            ([0, 2], 0),
            ([-1, 1], 1),
            ([0, 1], 0),
            ([1, 2, 3], -1),
            ([0, 2, 3], 0),
            ([-1, 1, 3], 1),
            ([-1, 0, 2], 2),
            ([0, 1, 2], 1),
        ],
    )
    def test(self, array: list[int], expected: int) -> None:
        assert magic_index(array) == expected
