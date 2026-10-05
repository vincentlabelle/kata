def search(array: list[int], value: int) -> int:
    """Linearly search `array` for `value`. This algorithm has a time
    complexity of O(n).

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
    for i, v in enumerate(array):
        if v == value:
            return i
    return -1
