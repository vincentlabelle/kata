def peak_valley(array: list[int]) -> None:
    """Given an array of integers, sort the array ito an alternating sequence of
    peaks and valleys.

    A "peak" is an element which is greater than or equal to the adjacent
    integers, and a "valley" is an element which is less than or equal to the
    adjacent integers.

    The algorithm must run in O(n) time.

    Parameters
    ----------
    array : list[int]
        The array to sort.
    """
    for i in range(1, len(array), 2):
        b = _index_of_max(array, i)
        array[b], array[i] = array[i], array[b]


def _index_of_max(array: list[int], i: int) -> int:
    if len(array) - 1 == i:
        if array[i] > array[i - 1]:
            return i
        return i - 1
    if array[i + 1] > array[i] and array[i + 1] > array[i - 1]:
        return i + 1
    if array[i] > array[i + 1] and array[i] > array[i - 1]:
        return i
    return i - 1
