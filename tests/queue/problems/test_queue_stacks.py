import pytest

from kata.queue.problems.queue_stacks import Queue


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
        queue.enqueue(2)
        assert queue.deque() == 1
        assert queue.deque() == 2


class TestQueuePeek:
    def test(self, queue: Queue[int]) -> None:
        assert queue.peek() is None
        queue.enqueue(0)
        assert queue.peek() == 0
        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.peek() == 0
        queue.deque()
        assert queue.peek() == 1
        queue.deque()
        assert queue.peek() == 2
        queue.deque()
        assert queue.peek() is None


class TestQueueDeque:
    def test_when_succeeds(self, queue: Queue[int]) -> None:
        queue.enqueue(0)
        assert queue.deque() == 0
        queue.enqueue(0)
        queue.enqueue(1)
        assert queue.deque() == 0
        queue.enqueue(2)
        assert queue.deque() == 1
        assert queue.deque() == 2

    def test_when_is_empty(self, queue: Queue[int]) -> None:
        with pytest.raises(RuntimeError, match="empty"):
            queue.deque()
