def conversion(a: int, b: int) -> int:
    """Count the number of bits to flip to convert `a` to `b`.

    Parameters
    ----------
    a : int
        First positive integer.
    b : int
        Second positive integer.

    Raises
    ------
    ValueError
        Raised when `a` or `b` is negative.

    Returns
    -------
    int
        The number of bits to flip.
    """
    _raise_if_negative(a, b)
    return _count(a, b)


def _raise_if_negative(a: int, b: int) -> None:
    if a < 0 or b < 0:
        message = "cannot count; a and b must be positive or zero"
        raise ValueError(message)


def _count(a: int, b: int) -> int:
    c = a ^ b
    count = 0
    while c != 0:
        if (c & 1) != 0:
            count += 1
        c >>= 1
    return count
