def sort(array: list[int]) -> None:
    """Sort `array` using quicksort. The time complexity is between O(nlog(n))
    and O(n^2).

    Quicksort uses a pivot (i.e., partitioning), and at each iteration puts all
    the elements lower than or equal to the pivot on the left-end side of the
    array slice (including the pivot itself).

    The time complexity can be O(n^2). An example, is if we choose the rightmost
    element as the pivot and the array is already sorted. Therefore, the pivot
    choice is important. To prevent this situation, it could be the median of
    the array slice.

    Parameters
    ----------
    array : list[int]
        The array to sort.
    """
    _qs(array, 0, len(array) - 1)


def _qs(array: list[int], lower: int, upper: int) -> None:
    if lower >= upper:
        return
    index = _partition(array, lower, upper)
    _qs(array, lower, index - 1)
    _qs(array, index + 1, upper)


def _partition(array: list[int], lower: int, upper: int) -> int:
    pivot, k = array[upper], lower
    for i in range(lower, upper + 1):
        if array[i] <= pivot:
            array[k], array[i] = array[i], array[k]
            k += 1
    return k - 1
