import pytest

from kata.recursion.problems.stack_boxes import stack_boxes


class TestStackBoxes:
    @pytest.mark.parametrize(
        "boxes, expected",
        [
            ([], 0),
            ([(1, 0, 0)], 1),
            ([(3, 3, 3), (3, 2, 2)], 3),
            ([(3, 3, 3), (2, 3, 2)], 3),
            ([(3, 3, 3), (2, 2, 3)], 3),
            ([(3, 3, 3), (3, 3, 3)], 3),
            ([(3, 3, 3), (2, 2, 2), (1, 1, 1)], 6),
            ([(1, 1, 1), (2, 2, 2), (3, 3, 3)], 6),
            ([(3, 15, 10), (2, 10, 20), (1, 10, 5)], 4),
            ([(4, 4, 4), (4, 4, 4), (3, 3, 3)], 7),
            ([(1, 2, 3), (3, 2, 1), (2, 3, 1)], 3),
            ([(5, 5, 5), (4, 6, 4), (3, 4, 3)], 8),
            ([(5, 5, 5), (4, 6, 4), (3, 4, 3), (2, 3, 3)], 8),
        ],
    )
    def test(self, boxes: list[tuple[int, int, int]], expected: int) -> None:
        assert stack_boxes(boxes) == expected
