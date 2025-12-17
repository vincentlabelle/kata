def sum_swap(one: list[int], two: list[int]) -> tuple[int, int] | None:
    """Find one number from each array that can be swapped to cause the two
    array sums to be equal. The indexes of those numbers must be returned.

    The algorithm must run in O(n + m) time.

    Parameters
    ----------
    one : list[int]
        First array.
    two : list[int]
        Second array.

    Returns
    -------
    tuple[int, int] | None
        The indexes of the values to swap, or `None` if there is no possible
        swap.
    """
    distance = sum(one) - sum(two)
    if distance == 0 or (distance % 2) == 1:
        return None

    offset = distance // 2
    map_: dict[int, int] = {v: i for i, v in enumerate(one)}
    for i, v in enumerate(two):
        if (v + offset) in map_:
            return (map_[v + offset], i)
    return None
