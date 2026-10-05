def multiply(a: int, b: int) -> int:
    """Multiply to positive integers without using the `*` operator.
    Only addition, substraction, and bit shifting can be used.

    The algorithm must run in O(log(s)) time, where s in the smaller of the two
    numbers.

    Parameters
    ----------
    a : int
        First number to multiply.
    b : int
        Second number to multiply.

    Raises
    ------
    ValueError
        Raised when `a` or `b` is negative.

    Returns
    -------
    int
        The result of the multiplication.
    """
    _raise_if_negative(a)
    _raise_if_negative(b)
    if b < a:
        return _multiply(a, b)
    return _multiply(b, a)


def _raise_if_negative(int_: int) -> None:
    if int_ < 0:
        message = "cannot multiply; a and b must be positive or zero"
        raise ValueError(message)


def _multiply(a: int, b: int) -> int:
    if b == 0:
        return 0
    res = _multiply(a, b >> 1) << 1
    if b & 1 == 1:
        res += a
    return res
