import pytest

from kata.array.problems.reverse import reverse


class TestReverse:
    @pytest.mark.parametrize(
        "array",
        [
            [],
            [1],
            [1, 2],
            [1, 2, 3],
            [1, 2, 3, 4],
        ],
    )
    def test(self, array: list[int]) -> None:
        expected = array[::-1]
        reverse(array)
        assert array == expected
