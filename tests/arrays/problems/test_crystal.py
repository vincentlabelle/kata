import pytest

from kata.arrays.problems.crystal import search


class TestSearch:
    @pytest.mark.parametrize(
        "breaks, expected",
        [
            ([], -1),
            ([False], -1),
            ([True], 0),
            ([True, True, True], 0),
            ([False, True, True], 1),
            ([False, False, True], 2),
            ([False, False, False], -1),
            ([True, True, True, True], 0),
            ([False, True, True, True], 1),
            ([False, False, True, True], 2),
            ([False, False, False, True], 3),
            ([False, False, False, False], -1),
            ([True, True, True, True, True], 0),
            ([False, True, True, True, True], 1),
            ([False, False, True, True, True], 2),
            ([False, False, False, True, True], 3),
            ([False, False, False, False, True], 4),
            ([False, False, False, False, False], -1),
        ],
    )
    def test(self, breaks: list[bool], expected: int) -> None:
        assert search(breaks) == expected
