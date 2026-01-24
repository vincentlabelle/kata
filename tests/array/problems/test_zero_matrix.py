import pytest

from kata.array.problems.zero_matrix import zero_matrix


class TestZeroMatrix:
    @pytest.mark.parametrize(
        "matrix, expected",
        [
            (
                [],
                [],
            ),
            (
                [[]],
                [[]],
            ),
            (
                [[], []],
                [[], []],
            ),
            (
                [[1]],
                [[1]],
            ),
            (
                [[0]],
                [[0]],
            ),
            (
                [[1, 2]],
                [[1, 2]],
            ),
            (
                [[1, 0]],
                [[0, 0]],
            ),
            (
                [[1], [2]],
                [[1], [2]],
            ),
            (
                [[1], [0]],
                [[0], [0]],
            ),
            (
                [[1, 2, 3], [3, 4, 5]],
                [[1, 2, 3], [3, 4, 5]],
            ),
            (
                [[1, 0, 3], [3, 4, 5]],
                [[0, 0, 0], [3, 0, 5]],
            ),
            (
                [[1, 0, 3], [4, 5, 6], [7, 0, 9]],
                [[0, 0, 0], [4, 0, 6], [0, 0, 0]],
            ),
        ],
    )
    def test(self, matrix: list[list[int]], expected: list[list[int]]) -> None:
        zero_matrix(matrix)
        assert matrix == expected
