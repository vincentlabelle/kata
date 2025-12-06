def search[T](array: list[T]) -> T | None:
    """Search for the first non-duplicated value in `array`. The time complexity
    of this algorithm is O(n).

    Parameters
    ----------
    array : list[T]
        Array in which to search.

    Raises
    ------
    TypeError
        Raised when `T` is not hashable.

    Returns
    -------
    T | None
        The first non-duplicated value, or `None` if all values are duplicated.
    """
    counter: dict[T, int] = {}
    for v in array:
        counter[v] = counter.get(v, 0) + 1

    for v in array:
        if counter[v] == 1:
            return v
    return None
