import pytest

from kata.bit.problems.draw_line import draw_line


class TestDrawLine:
    @pytest.fixture(scope="function")
    def screen(self) -> bytearray:
        return bytearray([0x00, 0x80, 0x01, 0x00, 0x00, 0x00])

    @pytest.mark.parametrize(
        "width, x1, x2, y, expected",
        [
            (
                3,
                0,
                0,
                0,
                bytearray([0x80, 0x80, 0x01, 0x00, 0x00, 0x00]),
            ),
            (
                3,
                7,
                7,
                0,
                bytearray([0x01, 0x80, 0x01, 0x00, 0x00, 0x00]),
            ),
            (
                3,
                1,
                6,
                0,
                bytearray([0x7E, 0x80, 0x01, 0x00, 0x00, 0x00]),
            ),
            (
                3,
                1,
                6,
                1,
                bytearray([0x00, 0x80, 0x01, 0x7E, 0x00, 0x00]),
            ),
            (
                3,
                9,
                14,
                1,
                bytearray([0x00, 0x80, 0x01, 0x00, 0x7E, 0x00]),
            ),
            (
                3,
                0,
                14,
                1,
                bytearray([0x00, 0x80, 0x01, 0xFF, 0xFE, 0x00]),
            ),
            (
                3,
                1,
                16,
                1,
                bytearray([0x00, 0x80, 0x01, 0x7F, 0xFF, 0x80]),
            ),
            (
                3,
                1,
                23,
                1,
                bytearray([0x00, 0x80, 0x01, 0x7F, 0xFF, 0xFF]),
            ),
            (
                3,
                8,
                15,
                0,
                bytearray([0x00, 0xFF, 0x01, 0x00, 0x00, 0x00]),
            ),
            (
                3,
                8,
                16,
                0,
                bytearray([0x00, 0xFF, 0x81, 0x00, 0x00, 0x00]),
            ),
        ],
    )
    def test_when_succeeds(
        self,
        screen: bytearray,
        width: int,
        x1: int,
        x2: int,
        y: int,
        expected: bytearray,
    ) -> None:
        draw_line(screen, width, x1, x2, y)
        assert screen == expected

    @pytest.mark.parametrize(
        "width, x1, x2, y",
        [
            (-1, 0, 0, 0),
            (4, 0, 0, 0),
            (3, -1, 0, 0),
            (3, 1, 0, 0),
            (3, 0, 24, 0),
            (3, 0, 0, -1),
            (3, 0, 0, 3),
        ],
    )
    def test_when_raises_value_error(
        self,
        screen: bytearray,
        width: int,
        x1: int,
        x2: int,
        y: int,
    ) -> None:
        with pytest.raises(ValueError):
            draw_line(screen, width, x1, x2, y)
