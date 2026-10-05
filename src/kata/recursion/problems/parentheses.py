def parentheses(n: int) -> list[str]:
    """Get all valid combinations of `n` pairs of parentheses.

    Parameters
    ----------
    n : int
        Number of pairs for which to get the combinations.

    Returns
    -------
    list[str]
        The combinations.
    """
    parens: list[str] = []
    if n > 0:
        _parentheses(n, n, "", parens)
    return parens


def _parentheses(
    lcount: int,
    rcount: int,
    paren: str,
    parens: list[str],
) -> None:
    if lcount < 0 or rcount < lcount:
        return
    if lcount <= 0 and rcount <= 0:
        parens.append(paren)
        return
    _parentheses(lcount - 1, rcount, paren + "(", parens)
    _parentheses(lcount, rcount - 1, paren + ")", parens)
