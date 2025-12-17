import pytest

from kata.array.problems.increasing_triplet import increasing_triplet


class TestIncreasingTriplet:
    @pytest.mark.parametrize(
        "array, expected",
        [
            ([], False),
            ([1], False),
            ([1, 2], False),
            ([3, 2, 1], False),
            ([1, 3, 2], False),
            ([3, 1, 2], False),
            ([1, 2, 3], True),
            ([8, 9, 7, 10], True),
            ([22, 25, 21, 18, 20, 17, 16, 21], True),
        ],
    )
    def test(self, array: list[int], expected: bool) -> None:
        assert increasing_triplet(array) == expected
