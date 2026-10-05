def draw_line(
    screen: bytearray,
    width: int,
    x1: int,
    x2: int,
    y: int,
) -> None:
    """Given a screen stored as an array of bytes, draw an horizontal line
    from (`x1`, `y`) to (`x2`, `y`).

    Parameters
    ----------
    screen : bytearray
        Screen as an array of bytes.
    width : int
        Width of the screen (in bytes).
    x1 : int
        Start column index (i.e., bit position).
    x2 : int
        End column index (i.e., bit position).
    y : int
        Row index.

    Raises
    ------
    ValueError
        Raised when `width` is negative or zero,
        when `x1` or `x2` is out of bounds,
        when `screen` has a incomplete row, or
        when `y` is out of bounds.
    """
    _raise_if_width_is_negative_or_zero(width)
    _raise_if_x_out_of_bounds(x1, x2, width)
    _raise_if_incomplete_row(screen, width)
    _raise_if_y_out_of_bounds(y, screen, width)
    _draw(screen, width, x1, x2, y)


def _raise_if_width_is_negative_or_zero(width: int) -> None:
    if width <= 0:
        message = "cannot draw; width must be strictly positive"
        raise ValueError(message)


def _raise_if_x_out_of_bounds(x1: int, x2: int, width: int) -> None:
    if not 0 <= x1 <= x2 < width * 8:
        message = "cannot draw; x1 or x2 is out of bounds"
        raise ValueError(message)


def _raise_if_incomplete_row(screen: bytearray, width: int) -> None:
    if len(screen) % width != 0:
        message = "cannot draw; screen has an incomplete row"
        raise ValueError(message)


def _raise_if_y_out_of_bounds(y: int, screen: bytearray, width: int) -> None:
    if not 0 <= y < len(screen) // width:
        message = "cannot draw; y is out of bounds"
        raise ValueError(message)


def _draw(
    screen: bytearray,
    width: int,
    x1: int,
    x2: int,
    y: int,
) -> None:
    sindex = width * y + x1 // 8
    eindex = width * y + x2 // 8
    smask = 0xFF >> (x1 % 8)
    emask = ~(0xFF >> (x2 % 8 + 1)) & 0xFF
    if sindex == eindex:
        screen[sindex] |= smask & emask
    else:
        screen[sindex] |= smask
        screen[eindex] |= emask
        for i in range(sindex + 1, eindex):
            screen[i] = 0xFF
