def insertion(n: int, m: int, *, i: int, j: int) -> int:
    """Given two integers (`n` and `m`) and two bit positions (`i` and `j`),
    insert `m` into `n` such that `m` starts at bit `j` and ends at bit `i`.

    We assume that the bits `j` through `i` have enough space to fit all of `m`.

    Parameters
    ----------
    n : int
        Integer into which to insert.
    m : int
        Integer to insert.
    i : int
        Beginning bit position.
    j : int
        Ending bit position.

    Raises
    ------
    ValueError
        Raised when `i` is not within [0, j].

    Returns
    -------
    int
        The new integer after the insertion.
    """
    _raise_if_invalid_positions(i, j)
    return _insert(n, m, i, j)


def _raise_if_invalid_positions(i: int, j: int) -> None:
    if not 0 <= i <= j:
        message = "cannot insert; i must be within [0, j]"
        raise ValueError(message)


def _insert(n: int, m: int, i: int, j: int) -> int:
    c = ~((-1 << i) ^ (-1 << (j + 1))) & n
    return c | (m << i)
