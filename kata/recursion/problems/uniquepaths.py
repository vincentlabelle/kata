from functools import lru_cache


@lru_cache
def solve(rows: int, columns: int) -> int:
    """Solve the unique paths problem. The time complexity of this algorithm is
    O(n * m).

    In the unique paths problem, you have a grid of `rows` and `columns` and you
    must calculate the number of possible "shortest" paths from the
    upper-leftmost square to the lower-rightmost square.

    Parameters
    ----------
    rows : int
        Number of rows in the grid.
    columns : int
        Number of columns in the grid.

    Returns
    -------
    int
        The number of possible "shortest" paths.
    """
    if rows <= 0 or columns <= 0 or rows == 1 and columns == 1:
        return 0
    if rows == 1 or columns == 1:
        return 1
    return solve(rows - 1, columns) + solve(rows, columns - 1)
