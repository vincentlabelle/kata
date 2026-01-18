def one_away(one: str, two: str) -> bool:
    """Given two strings, write a function to check if they are one (or zero)
    edit away. A edit is either inserting, removing or replacing a character.

    The algorithm must run in O(n) time (where n is the length of the longest
    string).

    Parameters
    ----------
    one : str
        The first string to verify.
    two : str
        The second string to verify.

    Returns
    -------
    bool
        `True` if the strings are one (or zero) edits away, else `False`.
    """
    if len(one) == len(two):
        return _is_one_away_when_match(one, two)
    if len(one) + 1 == len(two):
        return _is_one_away_when_mismatch(one, two)
    if len(one) - 1 == len(two):
        return _is_one_away_when_mismatch(two, one)
    return False


def _is_one_away_when_match(one: str, two: str) -> bool:
    count = 0
    for i in range(len(one)):
        if one[i] != two[i]:
            count += 1
    return count <= 1


def _is_one_away_when_mismatch(short: str, long: str) -> bool:
    i, j = 0, 0
    while i < len(short) and j < len(long):
        if short[i] != long[j]:
            if i != j:
                return False
            j += 1
        else:
            i += 1
            j += 1
    return True
