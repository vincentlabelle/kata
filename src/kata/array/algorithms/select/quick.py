def select(array: list[int], k: int) -> int:
    """Select the kth lowest value of `array` using quickselect. The time
    complexity is between O(n) and O(n^2).

    Like quicksort, quickselect uses partitioning (i.e., a pivot). However, it
    only recurses on one side of the array.

    The time complexity can be O(n^2) for the same reason as quicksort.

    Parameters
    ----------
    array : list[int]
        The array from which to select.
    k : int
        The value to select.

    Raises
    ------
    ValueError
        Raised when `k` is outside of bounds (i.e., outside of
        [0, `len(array)`[).

    Returns
    -------
    int
        The selected value.
    """
    _raise_if_out_of_bounds(array, k)
    return _select(array, 0, len(array) - 1, k)


def _raise_if_out_of_bounds(array: list[int], k: int) -> None:
    if k < 0 or k >= len(array):
        message = f"cannot select; k must be within [0, {len(array)}["
        raise ValueError(message)


def _select(array: list[int], lower: int, upper: int, k: int) -> int:
    if lower >= upper:
        return array[lower]
    return __select(array, lower, upper, k)


def __select(array: list[int], lower: int, upper: int, k: int) -> int:
    index = _partition(array, lower, upper)
    if k == index:
        return array[index]
    if k < index:
        return _select(array, lower, index - 1, k)
    return _select(array, index + 1, upper, k)


def _partition(array: list[int], lower: int, upper: int) -> int:
    pivot, k = array[upper], lower
    for i in range(lower, upper + 1):
        if array[i] <= pivot:
            array[k], array[i] = array[i], array[k]
            k += 1
    return k - 1
