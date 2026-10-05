from functools import lru_cache


def stack_boxes(boxes: list[tuple[int, int, int]]) -> int:
    """Given `boxes` of specific dimensions (i.e., height, width and
    depth), determine the height of the tallest possible stack of boxes.
    The boxes cannot be rotated and can only be stacked on top of one another
    if each box in the stack is strictly larger than the box above it in all
    dimensions.

    The algorithm must run in O(n^2) time.

    Parameters
    ----------
    boxes : list[tuple[int, int, int]]
        Boxes to stack; each box is represented by a `tuple` of dimensions in
        the following order: hight, width and depth.

    Returns
    -------
    int
        The height of the tallest possible stack of boxes.
    """
    max_ = 0
    boxes_ = tuple(sorted(boxes, key=lambda b: b[0], reverse=True))
    for i in range(len(boxes_)):
        height = _stack(boxes_, i)
        max_ = max(height, max_)
    return max_


@lru_cache
def _stack(boxes: tuple[tuple[int, int, int], ...], index: int) -> int:
    max_ = 0
    h, w, d = boxes[index]
    for i in range(index + 1, len(boxes)):
        h2, w2, d2 = boxes[i]
        if h2 < h and w2 < w and d2 < d:
            height = _stack(boxes, i)
            max_ = max(height, max_)
    return max_ + h
