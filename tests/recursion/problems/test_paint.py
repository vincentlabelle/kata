import pytest

from kata.recursion.problems.paint import Color, Point, paint


class TestPaint:
    @pytest.mark.parametrize(
        "screen, expected",
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
                [[Color.BLUE]],
                [[Color.BLUE]],
            ),
            (
                [[Color.RED]],
                [[Color.BLUE]],
            ),
            (
                [[Color.BLUE, Color.BLUE]],
                [[Color.BLUE, Color.BLUE]],
            ),
            (
                [[Color.RED, Color.GREEN]],
                [[Color.BLUE, Color.GREEN]],
            ),
            (
                [[Color.RED, Color.RED]],
                [[Color.BLUE, Color.BLUE]],
            ),
            (
                [
                    [Color.BLUE],
                    [Color.BLUE],
                ],
                [
                    [Color.BLUE],
                    [Color.BLUE],
                ],
            ),
            (
                [
                    [Color.RED],
                    [Color.GREEN],
                ],
                [
                    [Color.BLUE],
                    [Color.GREEN],
                ],
            ),
            (
                [
                    [Color.RED],
                    [Color.RED],
                ],
                [
                    [Color.BLUE],
                    [Color.BLUE],
                ],
            ),
            (
                [
                    [Color.RED, Color.GREEN, Color.RED],
                    [Color.RED, Color.GREEN, Color.RED],
                    [Color.RED, Color.RED, Color.RED],
                ],
                [
                    [Color.BLUE, Color.GREEN, Color.BLUE],
                    [Color.BLUE, Color.GREEN, Color.BLUE],
                    [Color.BLUE, Color.BLUE, Color.BLUE],
                ],
            ),
        ],
    )
    def test(
        self,
        screen: list[list[Color]],
        expected: list[list[Color]],
    ) -> None:
        paint(screen, Point(0, 0), Color.BLUE)
        assert screen == expected
