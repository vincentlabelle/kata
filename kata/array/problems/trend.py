import sys


def has_trend(array: list[int]) -> bool:
    """Verify if `array` contains an upward trend composed of three values.
    The time complexity of this operation is O(n).

    Parameters
    ----------
    array : list[int]
        Array to verify for an upward trend.

    Returns
    -------
    bool
        `True` if there's an upward trend, else `False`.
    """
    low, mid = sys.maxsize, sys.maxsize
    for v in array:
        if v <= low:
            low = v
        elif v <= mid:
            mid = v
        else:
            return True
    return False
