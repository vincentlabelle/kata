def string_rotation(one: str, two: str) -> bool:
    """Given two strings, verify if `two` is a rotation of `one`.

    The algorithm must run in O(n) time (assuming substring search is O(n)).

    Parameters
    ----------
    one : str
        The first string.
    two : str
        The second string.

    Returns
    -------
    bool
        `True` if `two` is a rotation of `one`, else `False`.
    """
    if len(one) != len(two):
        return False
    return one in (two + two)
