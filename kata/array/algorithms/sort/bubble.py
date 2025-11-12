def sort(array: list[int]) -> None:
    """Sort `array` using bubble sort. The time complexity is O(n^2).

    Bubble sort swaps elements of `array` such that after each iteration the
    largest remaining element is at the last slot.

    Parameters
    ----------
    array : list[int]
        The array to sort.
    """
    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
