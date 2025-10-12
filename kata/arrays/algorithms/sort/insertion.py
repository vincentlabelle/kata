def sort(array: list[int]) -> None:
    """Sort `array` using insertion sort. The time complexity is O(n^2).

    Insertion sort swaps elements of `array` such that after each iteration the
    current element is inserted at the index guaranteeing that the beginning of
    the array remains sorted.

    Parameters
    ----------
    array : list[int]
        The array to sort.
    """
    for i in range(1, len(array)):
        for j in range(i - 1, -1, -1):
            if array[j] <= array[j + 1]:
                break
            array[j], array[j + 1] = array[j + 1], array[j]
