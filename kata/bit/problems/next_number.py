def next_number(value: int) -> int:
    """Given a strictly positive integer, returns the next largest number that
    have the same number of 1 bits in their binary representation.

    Parameters
    ----------
    value : int
        Integer for which to get the next largest number.

    Raises
    ------
    ValueError
        Raised when `value` is negative or zero.

    Returns
    -------
    int
        The next largest number.
    """
    _raise_if_negative_or_zero(value)
    return _next(value)


def _raise_if_negative_or_zero(value: int) -> None:
    if value <= 0:
        message = "cannot obtain next number; value must be strictly positive"
        raise ValueError(message)


def _next(value: int) -> int:
    pivot = _find(value)
    value = _move_up(value, pivot)
    return _move_down(value, pivot)


def _find(value: int) -> int:
    i = 0
    while (value & (1 << i)) == 0:
        i += 1
    while (value & (1 << (i + 1))) != 0:
        i += 1
    return i


def _move_up(value: int, pivot: int) -> int:
    return _move(value, pivot, pivot + 1)


def _move(value: int, prev: int, new: int) -> int:
    return value & ~(1 << prev) | (1 << new)


def _move_down(value: int, pivot: int) -> int:
    i, j = pivot - 1, 0
    while i > j and (value & (1 << i)) != 0 and (value & (1 << j)) == 0:
        value = _move(value, i, j)
        i -= 1
        j += 1
    return value
