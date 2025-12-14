import sys


def maximum(array: list[int]) -> int:
    """Given an array of stock prices, find the greatest profit that could be
    made from a single buy following by a single sell transaction.

    The time complexity of this operation is O(n).

    Parameters
    ----------
    array : list[int]
        Prices over time.

    Returns
    -------
    int
        The greatest profit.
    """
    low, max_ = sys.maxsize, 0
    for value in array:
        if value < low:
            low = value
        elif (value - low) > max_:
            max_ = value - low
    return max_
