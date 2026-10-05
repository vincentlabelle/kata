from dataclasses import dataclass


@dataclass(frozen=True)
class Position:
    """Representation of a position in a matrix."""

    x: int
    y: int


def search_matrix(matrix: list[list[int]], value: int) -> Position | None:
    """Given a matrix in which each row and column is sorted in ascending
    order, find an element.

    Parameters
    ----------
    matrix : list[list[int]]
        The matrix in which to find the element.
    value : int
        The element to find.

    Raises
    ------
    ValueError
        Raised when the rows in `matrix` are not all of the same length.

    Returns
    -------
    Position | None
        The position of `value` in `matrix`, or `None` if `value` is not in
        `matrix`.
    """
    if len(matrix) == 0:
        return None
    _raise_if_not_matrix(matrix)
    return _search(
        matrix,
        Position(0, 0),
        Position(len(matrix) - 1, len(matrix[-1]) - 1),
        value,
    )


def _raise_if_not_matrix(matrix: list[list[int]]) -> None:
    if len({len(row) for row in matrix}) > 1:
        message = "cannot search; rows must be of the same length"
        raise ValueError(message)


def _search(
    matrix: list[list[int]],
    lower: Position,
    upper: Position,
    value: int,
) -> Position | None:
    if _is_outside(matrix, lower) or _is_outside(matrix, upper):
        return None

    # Search for the first position greater than `value`
    next_ = _search_diagonal(matrix, lower, upper, value)

    # The whole diagonal is greater than `value`
    if next_ == lower:
        return None

    # Found
    if matrix[next_.x - 1][next_.y - 1] == value:
        return Position(next_.x - 1, next_.y - 1)

    # Recurse
    found = _search(
        matrix,
        Position(lower.x, next_.y),
        Position(next_.x - 1, upper.y),
        value,
    )
    if found is None:
        found = _search(
            matrix,
            Position(next_.x, lower.y),
            Position(upper.x, next_.y - 1),
            value,
        )
    return found


def _is_outside(matrix: list[list[int]], position: Position) -> bool:
    return (
        position.x < 0
        or position.y < 0
        or position.x >= len(matrix)
        or position.y >= len(matrix[-1])
    )


def _search_diagonal(
    matrix: list[list[int]],
    lower: Position,
    upper: Position,
    value: int,
) -> Position:
    # Adjust `upper` in case the matrix is not square
    min_ = min(upper.x - lower.x, upper.y - lower.y)
    upper = Position(lower.x + min_, lower.y + min_)

    # Finds the first position on the diagonal which has a value greater
    # than `value`, or returns a position greater than `upper` if none exists
    while lower.x <= upper.x and lower.y <= upper.y:
        midpoint = Position(
            (lower.x + upper.x) // 2,
            (lower.y + upper.y) // 2,
        )
        if matrix[midpoint.x][midpoint.y] <= value:
            lower = Position(midpoint.x + 1, midpoint.y + 1)
        else:
            upper = Position(midpoint.x - 1, midpoint.y - 1)
    return lower
