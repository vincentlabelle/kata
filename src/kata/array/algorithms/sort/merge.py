def sort(array: list[int]) -> None:
    """Sort `array` using mergesort. The time complexity is O(nlog(n)).

    Mergesort recursively "divides" the array in half, sorts each half, and then
    merges them back together.

    Parameters
    ----------
    array : list[int]
        The array to sort.
    """
    other = [0] * len(array)
    _ms(array, other, 0, len(array) - 1)


def _ms(array: list[int], other: list[int], lower: int, upper: int) -> None:
    if lower >= upper:
        return
    midpoint = (lower + upper) // 2
    _ms(array, other, lower, midpoint)
    _ms(array, other, midpoint + 1, upper)
    _merge(array, other, lower, midpoint, upper)


def _merge(
    array: list[int],
    other: list[int],
    lower: int,
    midpoint: int,
    upper: int,
) -> None:
    # Copy left and right slices
    for i in range(lower, upper + 1):
        other[i] = array[i]

    # Compare and copy back elements
    left, right = lower, midpoint + 1
    current = lower
    while left <= midpoint and right <= upper:
        if other[left] <= other[right]:
            array[current] = other[left]
            left += 1
        else:
            array[current] = other[right]
            right += 1
        current += 1

    # Copy remainder from the left slice if any
    while left <= midpoint:
        array[current] = other[left]
        left += 1
        current += 1
