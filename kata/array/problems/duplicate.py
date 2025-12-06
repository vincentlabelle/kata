def search[T](array: list[T]) -> T | None:
    """Search for the first duplicated value in an array. The time complexity of
    this operation is O(n).

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
        The first duplicated value, or `None` if there are no duplicated values.
    """
    set_ = set()
    for v in array:
        if v in set_:
            return v
        set_.add(v)
    return None
