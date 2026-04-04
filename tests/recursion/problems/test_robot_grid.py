import pytest

from kata.recursion.problems.robot_grid import Position, robot_grid


class TestRobotGrid:
    @pytest.mark.parametrize(
        "grid, expected",
        [
            ([], []),
            ([[]], []),
            ([[], []], []),
            (
                [
                    [False],
                ],
                [],
            ),
            (
                [
                    [True, True, False],
                ],
                [],
            ),
            (
                [
                    [True],
                    [True],
                    [False],
                ],
                [],
            ),
            (
                [
                    [True, True, True],
                    [True, True, False],
                    [True, False, True],
                ],
                [],
            ),
            (
                [
                    [True],
                ],
                [Position(0, 0)],
            ),
            (
                [
                    [True, True],
                ],
                [Position(0, 0), Position(0, 1)],
            ),
            (
                [
                    [True],
                    [True],
                ],
                [Position(0, 0), Position(1, 0)],
            ),
            (
                [
                    [True, True, True],
                    [True, False, True],
                    [True, False, True],
                    [True, False, True],
                    [True, False, True],
                ],
                [
                    Position(0, 0),
                    Position(0, 1),
                    Position(0, 2),
                    Position(1, 2),
                    Position(2, 2),
                    Position(3, 2),
                    Position(4, 2),
                ],
            ),
        ],
    )
    def test(self, grid: list[list[bool]], expected: list[Position]) -> None:
        assert robot_grid(grid) == expected
