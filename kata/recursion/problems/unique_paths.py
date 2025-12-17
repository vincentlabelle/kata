from functools import lru_cache


@lru_cache
def unique_paths(rows: int, columns: int) -> int:
    """Given a grid of `rows` and `columns`, calculate the number of possible
    "shortest" paths from the upper-leftmost square to the lower-rightmost
    square.

    The algorithm must run in O(n * m).

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
    return unique_paths(rows - 1, columns) + unique_paths(rows, columns - 1)
