from dataclasses import dataclass


@dataclass(frozen=True)
class Position:
    """Representation of a position in a grid."""

    x: int
    y: int


_DIRECTIONS = (Position(1, 0), Position(0, 1))


def robot_grid(grid: list[list[bool]]) -> list[Position]:
    """Given a robot sitting on the upper left corner of a grid, find a path for
    the robot to the bottom right corner of the grid. The robot can only move
    right or down and certain cells are "off limits".

    The algorithm must run in O(n * m) time, where n is the number of rows
    and m is the number of columns.

    Parameters
    ----------
    grid : list[list[bool]]
        Grid for which to find a path; cells on which the robot can step are
        represented by `True`.

    Returns
    -------
    list[Position]
        The path.
    """
    current = Position(0, 0)
    seen: set[Position] = set()
    if not _can_move_to(current, grid, seen):
        return []
    path: list[Position] = []
    _find(current, grid, seen, path)
    return path


def _can_move_to(
    next_: Position,
    grid: list[list[bool]],
    seen: set[Position],
) -> bool:
    return (
        next_.x < len(grid)
        and next_.y < len(grid[next_.x])
        and grid[next_.x][next_.y]
        and next_ not in seen
    )


def _find(
    current: Position,
    grid: list[list[bool]],
    seen: set[Position],
    path: list[Position],
) -> bool:
    seen.add(current)
    path.append(current)
    if _is_found(current, grid):
        return True
    for direction in _DIRECTIONS:
        next_ = Position(current.x + direction.x, current.y + direction.y)
        if _can_move_to(next_, grid, seen) and _find(next_, grid, seen, path):
            return True
    path.pop()
    return False


def _is_found(current: Position, grid: list[list[bool]]) -> bool:
    return current.x == (len(grid) - 1) and current.y == (len(grid[-1]) - 1)
