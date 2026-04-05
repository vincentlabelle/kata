def power_set(set_: set[int]) -> list[set[int]]:
    """Return all subsets of `set_`.

    The algorithm must run in O(n * 2^n) time.

    Parameters
    ----------
    set_ : set[int]
        Set for which to return the subsets.

    Returns
    -------
    list[set[int]]
        The subsets of `set_`.
    """
    subs: list[set[int]] = []
    _power(set_.copy(), subs)
    return subs


def _power(set_: set[int], subs: list[set[int]]) -> None:
    if len(set_) == 0:
        subs.append(set())
        return
    value = set_.pop()
    _power(set_, subs)
    for i in range(len(subs)):
        subs.append({*subs[i], value})
