def sparse_search(array: list[str], value: str) -> int:
    """Given a sorted array of strings that is interspersed with emtpy strings,
    write the method to find the location of a given string.

    The algorithm must run in O(n) time.

    Parameters
    ----------
    array : list[str]
        The array to search.
    value : str
        The value to search for.

    Raises
    ------
    ValueError
        Raised when `value` is empty.

    Returns
    -------
    int
        The position of `value` in `array`, or `-1` if `value` isn't in array.
    """
    _raise_if_empty(value)
    return _search(array, value)


def _raise_if_empty(value: str) -> None:
    if value == "":
        message = "cannot search; value cannot be empty"
        raise ValueError(message)


def _search(array: list[str], value: str) -> int:
    lower, upper = 0, len(array) - 1
    while lower <= upper:
        # Get the midpoint, the index of the next non-empty string starting from
        # the midpoint, and whether the next non-empty string is on the left
        # side of the midpoint
        midpoint = (lower + upper) // 2
        is_left, next_ = _next(array, lower, midpoint, upper)

        # Only empty strings
        if next_ == -1:
            return -1

        # Found
        if array[next_] == value:
            return next_

        # Reduce search space
        if array[next_] > value:
            upper = (next_ if is_left else midpoint) - 1
        else:
            lower = (midpoint if is_left else next_) + 1
    return -1


def _next(
    array: list[str],
    lower: int,
    midpoint: int,
    upper: int,
) -> tuple[bool, int]:
    for i in range(midpoint, lower - 1, -1):
        if array[i] != "":
            return True, i
    for i in range(midpoint + 1, upper + 1):
        if array[i] != "":
            return False, i
    return True, -1
