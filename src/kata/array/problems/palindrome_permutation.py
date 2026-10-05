def palindrome_permutation(str_: str) -> bool:
    """Given a string, write a function to check if it is a permutation of a
    palindrome. The palindrome doesn't need to be limited to just dictionary
    words. Ignore casing and non-letter characters.

    The algorithm must run in O(n) time.

    Parameters
    ----------
    str_ : str
        String to verify if it is a permutation of a palindrome.

    Returns
    -------
    bool
        `True` if `str_` is a permutation of a palindrome, else `False`.
    """
    str__ = _remove_non_alpha(str_)
    counts = _count_by_char(str__)
    return _count_uneven(counts) <= 1


def _remove_non_alpha(str_: str) -> str:
    return "".join(char.lower() for char in str_ if char.isalpha())


def _count_by_char(str_: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for char in str_:
        counts[char] = counts.get(char, 0) + 1
    return counts


def _count_uneven(counts: dict[str, int]) -> int:
    return sum(1 for count in counts.values() if count % 2 != 0)
