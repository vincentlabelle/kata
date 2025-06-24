import pytest

from kata.linked.queue import Queue


@pytest.fixture
def queue() -> Queue[int]:
    return Queue()


class TestQueueEnqueue:
    def test(self, queue: Queue[int]) -> None:
        queue.enqueue(0)
        assert queue.deque() == 0
        queue.enqueue(0)
        queue.enqueue(1)
        assert queue.deque() == 0
        assert queue.deque() == 1


class TestQueuePeek:
    def test(self, queue: Queue[int]) -> None:
        assert queue.peek() is None
        queue.enqueue(0)
        assert queue.peek() == 0
        queue.enqueue(1)
        assert queue.peek() == 0
        queue.deque()
        assert queue.peek() == 1
        queue.deque()
        assert queue.peek() is None


class TestQueueDeque:
    def test_when_succeeds(self, queue: Queue[int]) -> None:
        queue.enqueue(0)
        assert queue.deque() == 0
        queue.enqueue(0)
        queue.enqueue(1)
        assert queue.deque() == 0
        assert queue.deque() == 1

    def test_when_is_empty(self, queue: Queue[int]) -> None:
        with pytest.raises(RuntimeError, match="empty"):
            queue.deque()


class TestQueueEq:
    @pytest.fixture
    def other(self) -> Queue[int]:
        return Queue()

    @pytest.mark.parametrize(
        "values",
        [
            [],
            [0, 1],
        ],
    )
    def test_when_equal(
        self,
        queue: Queue[int],
        other: Queue[int],
        values: list[int],
    ) -> None:
        for v in values:
            queue.enqueue(v)
            other.enqueue(v)
        assert other == queue

    @pytest.mark.parametrize(
        "queue_values, other_values",
        [
            ([], [0]),
            ([0, 1], [0, 2]),
        ],
    )
    def test_when_different_head(
        self,
        queue: Queue[int],
        other: Queue[int],
        queue_values: list[int],
        other_values: list[int],
    ) -> None:
        for v in queue_values:
            queue.enqueue(v)
        for v in other_values:
            other.enqueue(v)
        assert other != queue

    def test_when_different_type(self, queue: Queue[int]) -> None:
        assert queue != "a"


class TestQueueStr:
    @pytest.mark.parametrize(
        "values, expected",
        [
            ([], "||"),
            ([0, 1], "|0->1|"),
        ],
    )
    def test(self, queue: Queue[int], values: list[int], expected: str) -> None:
        for v in values:
            queue.enqueue(v)
        assert str(queue) == expected


class TestQueueRepr:
    def test(self, queue: Queue[int]) -> None:
        assert repr(queue) == f"{queue.__class__.__name__}({queue})"
