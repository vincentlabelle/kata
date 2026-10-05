def reverse[T](array: list[T]) -> None:
    """Reverse `array` in-place with constant space in linear time.

    Parameters
    ----------
    array : list[T]
        Array to reverse.
    """
    lower, upper = 0, len(array) - 1
    while lower < upper:
        array[lower], array[upper] = array[upper], array[lower]
        lower, upper = lower + 1, upper - 1
