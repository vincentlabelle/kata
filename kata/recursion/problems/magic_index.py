def magic_index(array: list[int]) -> int:
    """Given an array of sorted distinct integers, find a magic index, if one
    exits, in the array. A magic index is defined as an index such that
    `array[i] == i`.

    The algorithm must run in O(log(n)) time.

    Parameters
    ----------
    array : list[int]
        Array for which to find the magic index.

    Returns
    -------
    int
        The index of the magic index or `-1` if none exists.
    """
    lower, upper = 0, len(array) - 1
    while lower <= upper:
        # Obtain midpoint index
        mid = (lower + upper) // 2

        # Found
        if array[mid] == mid:
            return mid

        # Reduce search space
        if array[mid] < mid:
            lower = mid + 1
        else:
            upper = mid - 1
    return -1
