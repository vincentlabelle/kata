from copy import copy


def queens(n: int) -> list[list[int]]:
    """Determine all the ways to arrange `n` queens on an `n`x`n` chess board
    so that none of them share the same row, column or diagonal.

    Parameters
    ----------
    n : int
        Size of the board, and number of queens.

    Returns
    -------
    list[list[int]]
        The ways to arrange the queens.
    """
    all_: list[list[int]] = []
    if n <= 0:
        return all_
    _queens(0, [0] * n, all_)
    return all_


def _queens(row: int, current: list[int], all_: list[list[int]]) -> None:
    if row == len(current):
        all_.append(copy(current))
        return
    for column in range(len(current)):
        if _is_valid(row, column, current):
            current[row] = column
            _queens(row + 1, current, all_)


def _is_valid(row1: int, column1: int, current: list[int]) -> bool:
    for row2 in range(row1):
        column2 = current[row2]
        if (column2 == column1) or (abs(column2 - column1) == abs(row2 - row1)):
            return False
    return True
