def intersect[T](a: list[T], b: list[T]) -> list[T]:
    """Get the intesection of two arrays. The time complexity of this algorithm
    is O(n + m).

    Parameters
    ----------
    a : list[T]
        The first array.
    b : list[T]
        The second array.

    Raises
    ------
    TypeError
        Raised when `T` is not hashable.

    Returns
    -------
    list[T]
        The intersection.
    """
    set_ = set(a)
    return [v for v in b if v in set_]
