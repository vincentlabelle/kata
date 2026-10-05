from functools import lru_cache


@lru_cache
def triple_step(n: int) -> int:
    """Given a staircase of `n` steps, count how many possible ways a person
    can run up the stairs if the person can hop either 1, 2, or 3 steps at a
    time.

    The algorithm must run in O(n) time.

    Parameters
    ----------
    n : int
        Number of steps in the staircase.

    Returns
    -------
    int
        The number of ways.
    """
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 4
    return triple_step(n - 1) + triple_step(n - 2) + triple_step(n - 3)
