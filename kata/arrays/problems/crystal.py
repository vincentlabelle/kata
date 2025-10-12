import math


def search(breaks: list[bool]) -> int:
    """Search for the floor in the two crystal balls problem. The time
    complexity of this algorithm is O(sqrt(n)) which is the optimal solution.

    In the two crystal balls problem, you are looking for the first floor in
    a building at which a crystal ball would break if it was dropped from that
    floor.

    Parameters
    ----------
    breaks : list[bool]
        Indicators of whether a ball would break at a given floor.

    Returns
    -------
    int
        Index of the first floor at which a crytal ball would break, or `-1`
        if there are no such floor.
    """
    if len(breaks) == 0:
        return -1
    return _search(breaks)


def _search(breaks: list[bool]) -> int:
    size = _get_jump_size(breaks)
    upper = _search_for_upper(breaks, size)
    return _search_for_actual(breaks, size, upper)


def _get_jump_size(breaks: list[bool]) -> int:
    size = math.sqrt(len(breaks))
    return math.floor(size)


def _search_for_upper(breaks: list[bool], size: int) -> int:
    for i in range(size - 1, len(breaks), size):
        if breaks[i]:
            return i
    return len(breaks) - 1


def _search_for_actual(breaks: list[bool], size: int, upper: int) -> int:
    for i in range(upper - size + 1, len(breaks)):
        if breaks[i]:
            return i
    return -1
