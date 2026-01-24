def rotate_matrix(matrix: list[list[int]]) -> None:
    """Given an square matrix, rotate (in-place) the matrix by 90 degrees
    (clockwise).

    The algorithm must run in O(n) time where n is the number of elements
    in the matrix, and O(1) space.

    Parameters
    ----------
    matrix : list[list[int]]
        The matrix to rotate.

    Raises
    ------
    ValueError
        Raised when `matrix` isn't a square matrix.
    """
    if len(matrix) == 0:
        return
    _raise_if_not_matrix(matrix)
    _raise_if_not_square(matrix)
    _rotate(matrix)


def _raise_if_not_matrix(matrix: list[list[int]]) -> None:
    if any(len(row) != len(matrix[0]) for row in matrix):
        message = (
            "cannot rotate; matrix must have the same number of columns by row"
        )
        raise ValueError(message)


def _raise_if_not_square(matrix: list[list[int]]) -> None:
    if len(matrix) != len(matrix[0]):
        message = "cannot rotate; matrix must be square"
        raise ValueError(message)


def _rotate(matrix: list[list[int]]) -> None:
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp
