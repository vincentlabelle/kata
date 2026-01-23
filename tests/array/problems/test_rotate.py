import pytest

from kata.array.problems.rotate import rotate


class TestRotate:
    @pytest.mark.parametrize(
        "matrix, expected",
        [
            (
                [],
                [],
            ),
            (
                [[1]],
                [[1]],
            ),
            (
                [[1, 2], [3, 4]],
                [[3, 1], [4, 2]],
            ),
            (
                [[1, 2, 3], [3, 4, 5], [6, 7, 8]],
                [
                    [6, 3, 1],
                    [7, 4, 2],
                    [8, 5, 3],
                ],
            ),
        ],
    )
    def test_when_succeeds(
        self,
        matrix: list[list[int]],
        expected: list[list[int]],
    ) -> None:
        actual = rotate(matrix)
        assert actual == expected

    @pytest.mark.parametrize(
        "matrix",
        [
            [[]],
            [[], []],
            [[1], [2]],
            [[], [2]],
            [[1], []],
        ],
    )
    def test_when_raises_value_error(self, matrix: list[list[int]]) -> None:
        with pytest.raises(ValueError):
            rotate(matrix)
