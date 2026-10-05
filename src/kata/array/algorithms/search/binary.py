def search(array: list[int], value: int) -> int:
    """Search `array` for `value` using binary search. The `array` must be
    sorted, to ensure the proper result is obtained. The time complexity is
    O(log(n)), because at worst we must divide `array` log(n) times.

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
    lower, upper = 0, len(array) - 1
    while lower <= upper:
        # Obtain midpoint index
        midpoint = lower + (upper - lower) // 2

        # Found
        if array[midpoint] == value:
            return midpoint

        # Reduce search space
        if array[midpoint] > value:
            upper = midpoint - 1
        else:
            lower = midpoint + 1
    return -1
