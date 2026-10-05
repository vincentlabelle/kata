def is_permutation(one: str, two: str) -> bool:
    """Given two strings, verify if one is a permutation of the other.

    The algorithm must run in O(n) time (where n is the length of the longest
    string).

    Parameters
    ----------
    one : str
        The first string for which to verify.
    two : str
        The second string for which to verify.

    Returns
    -------
    bool
        `True` if `two` is a permutation of `one`, else `False`
    """
    if len(one) != len(two):
        return False
    return _count(one) == _count(two)


def _count(str_: str) -> dict[str, int]:
    count: dict[str, int] = {}
    for char in str_:
        count[char] = count.get(char, 0) + 1
    return count
