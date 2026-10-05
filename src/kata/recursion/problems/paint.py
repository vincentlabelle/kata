from dataclasses import dataclass
from enum import Enum, auto


class Color(Enum):
    """Representation of screen colors."""

    RED = auto()
    GREEN = auto()
    BLUE = auto()


@dataclass(frozen=True)
class Point:
    """Representation of a point on a screen."""

    x: int
    y: int


_DIRECTIONS = (
    Point(1, 0),
    Point(-1, 0),
    Point(0, 1),
    Point(0, -1),
)


def paint(screen: list[list[Color]], point: Point, new: Color) -> None:
    """Given a screen, a point and a new color, fill in the surrounding area
    until the color changes from the original color.

    The algorithm must run in O(n * m) time, where n is the number of rows
    and m is the number of columns.

    Parameters
    ----------
    screen : list[list[Color]]
        Screen to paint.
    point : Point
        Initial position to paint from.
    new : Color
        Color to paint.
    """
    if not _is_inside(screen, point):
        return
    previous = screen[point.x][point.y]
    if previous == new:
        return
    _paint(screen, point, new, previous)


def _is_inside(screen: list[list[Color]], point: Point) -> bool:
    return 0 <= point.x < len(screen) and 0 <= point.y < len(screen[point.x])


def _paint(
    screen: list[list[Color]],
    point: Point,
    new: Color,
    previous: Color,
) -> None:
    screen[point.x][point.y] = new
    for direction in _DIRECTIONS:
        moved = Point(point.x + direction.x, point.y + direction.y)
        if _can_paint(screen, moved, previous):
            _paint(screen, moved, new, previous)


def _can_paint(
    screen: list[list[Color]],
    moved: Point,
    previous: Color,
) -> bool:
    return _is_inside(screen, moved) and screen[moved.x][moved.y] == previous
