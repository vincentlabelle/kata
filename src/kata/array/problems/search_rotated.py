def search_rotated(array: list[int], value: int) -> int:
    """Given a sorted array that has been rotated an unknown number of times,
    find a value in the array.

    The runtime of the algorithm must be between O(log(n)) and O(n).

    Parameters
    ----------
    array : list[int]
        The array to search.
    value : int
        The value to search for.

    Returns
    -------
    int
        The position of `value` in `array`, or `-1` if `value` isn't in `array`.
    """
    return _search(array, 0, len(array) - 1, value)


def _search(array: list[int], lower: int, upper: int, value: int) -> int:
    # Not Found
    if upper < lower:
        return -1

    # Found
    midpoint = (lower + upper) // 2
    if array[midpoint] == value:
        return midpoint

    # Left side is sorted
    if array[lower] < array[midpoint]:
        if array[lower] <= value < array[midpoint]:
            return _search(array, lower, midpoint - 1, value)
        else:
            return _search(array, midpoint + 1, upper, value)
    # Right side is sorted
    elif array[midpoint] < array[upper]:
        if array[midpoint] < value <= array[upper]:
            return _search(array, midpoint + 1, upper, value)
        else:
            return _search(array, lower, midpoint - 1, value)
    # Values are duplicated on at least one side
    else:
        index = -1
        if array[lower] == array[midpoint]:
            index = _search(array, midpoint + 1, upper, value)
        if index == -1 and array[midpoint] == array[upper]:
            index = _search(array, lower, midpoint - 1, value)
        return index
