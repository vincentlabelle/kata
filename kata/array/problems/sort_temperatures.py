def sort_temperatures(array: list[int]) -> list[int]:
    """Sort an array of temperature readings for healthy people (i.e., from
    97.0 to 99.0 F with temperatures represented as `int`) in linear time.

    The algorithm used to solve this problem is known as counting sort.

    Parameters
    ----------
    array : list[int]
        Array of readings to sort.

    Returns
    -------
    list[int]
        Sorted array.
    """
    map_: dict[int, int] = {}
    for v in array:
        map_[v] = map_.get(v, 0) + 1

    new = []
    for v in range(970, 991):
        if v in map_:
            for _ in range(map_[v]):
                new.append(v)
    return new
