def is_unique(str_: str) -> bool:
    """Implement an algorithm to determine if a string has all unique
    characters based on the ASCII character set.

    The algorithm must run in O(n) time and O(1) space.

    Parameters
    ----------
    str_ : str
        String to determine the uniqueness for.

    Returns
    -------
    bool
        `True` if `str_` has all unique characters, else `False`.
    """
    for i in range(128):
        count = str_.count(chr(i))
        if count > 1:
            return False
    return True
