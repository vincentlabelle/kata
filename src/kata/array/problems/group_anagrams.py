def group_anagrams(array: list[str]) -> None:
    """Sort an array of strings such that all the anagrams are next to each
    other.

    The time complexity of this algorithm is O(a * slog(s)) where a is the size
    of the array and s is the length of the longest string.

    Parameters
    ----------
    array : list[str]
        Array to sort.
    """
    groups = _group(array)
    _copy(array, groups)


def _group(array: list[str]) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = {}
    for s in array:
        key = _key(s)
        if key in groups:
            groups[key].append(s)
        else:
            groups[key] = [s]
    return groups


def _key(s: str) -> str:
    return "".join(sorted(s))


def _copy(array: list[str], groups: dict[str, list[str]]) -> None:
    i = 0
    for value in groups.values():
        for s in value:
            array[i] = s
            i += 1
