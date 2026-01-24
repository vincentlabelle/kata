def zero_matrix(matrix: list[list[int]]) -> None:
    """Search `matrix` for any element equal to zero, and for any such element
    set its entire row and column to zero.

    The algorithm must run in O(n) time where n is the number of elements
    in `matrix`.

    Parameters
    ----------
    matrix : list[list[int]]
        Matrix for which to set some rows and columns to zero.
    """
    rows, cols = _search(matrix)
    _set_zero(matrix, rows, cols)


def _search(matrix: list[list[int]]) -> tuple[set[int], set[int]]:
    rows: set[int] = set()
    cols: set[int] = set()
    for i, row in enumerate(matrix):
        for j, v in enumerate(row):
            if v == 0:
                rows.add(i)
                cols.add(j)
    return rows, cols


def _set_zero(matrix: list[list[int]], rows: set[int], cols: set[int]) -> None:
    for i, row in enumerate(matrix):
        for j in range(len(row)):
            if i in rows or j in cols:
                row[j] = 0
