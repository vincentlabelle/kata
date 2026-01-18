def compression(str_: str) -> str:
    """Perform basic string compression using the counts of repeated characters.
    If the compressed string wouldn't become smaller than the original string,
    the original string is returned.

    The algorithm must run in O(n) time.

    Parameters
    ----------
    str_ : str
        The string to compress.

    Returns
    -------
    str
        The compressed string.
    """
    compressed = _compress(str_)
    if len(compressed) < len(str_):
        return compressed
    return str_


def _compress(str_: str) -> str:
    compressed = []
    count = 0
    for i in range(len(str_)):
        count += 1
        if (i + 1) >= len(str_) or str_[i] != str_[i + 1]:
            compressed.append(f"{str_[i]}{count}")
            count = 0
    return "".join(compressed)
