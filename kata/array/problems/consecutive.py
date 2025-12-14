def get_longest(array: list[int]) -> int:
    """Get the length of the longest consecutive sequence of values in `array`.
    The consecutive values do not have to be adjacent.

    The time complexity of this operation is O(n).

    Parameters
    ----------
    array : list[int]
        Array for which to get the length.

    Returns
    -------
    int
        The length of the longest consecutive sequence.
    """
    max_, set_ = 0, set(array)
    for v in set_:
        if (v - 1) not in set_:  # check for beginning of sequence
            len_ = _len(set_, v)
            if len_ > max_:
                max_ = len_
    return max_


def _len(set_: set[int], v: int) -> int:
    len_, next_ = 1, v + 1
    while next_ in set_:
        len_, next_ = len_ + 1, next_ + 1
    return len_
