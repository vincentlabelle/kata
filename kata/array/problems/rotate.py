def rotate(matrix: list[list[int]]) -> list[list[int]]:
    """Given an square matrix, rotate the matrix by 90 degrees (clockwise).

    The algorithm must run in O(n) time where n is the number of elements
    in the matrix.

    Parameters
    ----------
    matrix : list[list[int]]
        The matrix to rotate.

    Raises
    ------
    ValueError
        Raised when `matrix` isn't a square matrix.

    Returns
    -------
    list[list[int]]
        The rotated matrix.
    """
    if len(matrix) == 0:
        return matrix
    _raise_if_not_matrix(matrix)
    _raise_if_not_square(matrix)
    return _rotate(matrix)


def _raise_if_not_matrix(matrix: list[list[int]]) -> None:
    if len({len(row) for row in matrix}) > 1:
        message = (
            "cannot rotate; matrix must have the same number of columns by row"
        )
        raise ValueError(message)


def _raise_if_not_square(matrix: list[list[int]]) -> None:
    if len(matrix) != len(matrix[0]):
        message = "cannot rotate; matrix must be square"
        raise ValueError(message)


def _rotate(matrix: list[list[int]]) -> list[list[int]]:
    new = []
    for j in range(len(matrix[0])):
        row = []
        for i in range(len(matrix) - 1, -1, -1):
            row.append(matrix[i][j])
        new.append(row)
    return new
