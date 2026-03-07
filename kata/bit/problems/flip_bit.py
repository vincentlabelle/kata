def flip_bit(value: int) -> int:
    """Given a positive integer for which you can flip exactly one bit from 0
    to 1, find the length of the longest sequence of 1s which can be created.

    Parameters
    ----------
    value : int
        Integer for which one bit can be flipped.

    Raises
    ------
    ValueError
        Raised when `value` is negative.

    Returns
    -------
    int
        The length of the longest sequence.
    """
    _raise_if_negative(value)
    return _flip(value)


def _raise_if_negative(value: int) -> None:
    if value < 0:
        message = "cannot flip; value must be positive or zero"
        raise ValueError(message)


def _flip(value: int) -> int:
    v = value
    previous, current, max_ = 0, 0, 1
    while v != 0:
        if (v & 1) == 1:
            current += 1
        else:
            previous = 0
            if (v & 2) == 2:
                previous = current
            current = 0
        max_ = max(current + previous + 1, max_)
        v = v >> 1
    return max_
