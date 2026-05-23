import pytest

from kata.array.problems.search_matrix import Position, search_matrix


class TestSearchMatrix:
    @pytest.mark.parametrize(
        "matrix",
        [
            [],
            [[]],
            [[], []],
            [[1]],
            [[1, 2, 3]],
            [
                [1],
                [2],
                [3],
            ],
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
                [13, 14, 15, 16],
            ],
        ],
    )
    def test_when_succeeds(self, matrix: list[list[int]]) -> None:
        min_, max_ = -1, -1
        for i, row in enumerate(matrix):
            for j, value in enumerate(row):
                if value < min_:
                    min_ = value
                if value > max_:
                    max_ = value
                assert search_matrix(matrix, value) == Position(i, j)
        assert search_matrix(matrix, min_ - 1) is None
        assert search_matrix(matrix, max_ + 1) is None

    @pytest.mark.parametrize(
        "matrix",
        [
            [[0], []],
            [[], [0]],
            [[0, 1], [0], [1]],
            [[0, 1], [0], [1, 0]],
        ],
    )
    def test_when_raises_value_error(self, matrix: list[list[int]]) -> None:
        with pytest.raises(ValueError):
            search_matrix(matrix, 0)
