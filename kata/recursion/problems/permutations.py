def permutations(s: str) -> list[str]:
    """Compute all the permutations of a string of unique characters.

    The algorithm must run in O(n^2 * n!) time.

    Parameters
    ----------
    s : str
        String for which to compute the permutations.

    Returns
    -------
    list[str]
        The permutations.
    """
    if len(s) == 0:
        return []
    return _permutations(s)


def _permutations(s: str) -> list[str]:
    if len(s) == 1:
        return [s]
    perms = []
    for perm in _permutations(s[1:]):
        for i in range(len(perm) + 1):
            perms.append(perm[:i] + s[0] + perm[i:])
    return perms
