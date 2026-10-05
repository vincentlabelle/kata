from functools import lru_cache


def coins(n: int) -> int:
    """Given an infinite number of quarters, dimes, nickels and pennies,
    determine the number of ways of representing `n` cents.

    Parameters
    ----------
    n : int
        Number of cents to represent with coins.

    Returns
    -------
    int
        The number of ways.
    """
    if n <= 0:
        return 0
    return _count(n, (25, 10, 5, 1), 0)


@lru_cache
def _count(n: int, coins: tuple[int, ...], index: int) -> int:
    coin = coins[index]
    if index == len(coins) - 1:
        return 1 if n % coin == 0 else 0
    count = 0
    for times in range(0, n // coin + 1):
        count += _count(n - times * coin, coins, index + 1)
    return count
