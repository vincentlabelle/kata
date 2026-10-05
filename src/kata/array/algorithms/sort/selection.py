def sort(array: list[int]) -> None:
    """Sort `array` using selection sort. The time complexity is O(n^2).

    Selection sort swaps elements of `array` such that after each iteration the
    smallest remaining element is at the first available slot.

    Parameters
    ----------
    array : list[int]
        The array to sort.
    """
    for i in range(len(array) - 1):
        minimum = i
        for j in range(i + 1, len(array)):
            if array[j] < array[minimum]:
                minimum = j
        array[i], array[minimum] = array[minimum], array[i]
