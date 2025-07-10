import pytest

from kata.heaps.minimum import MinHeap


class TestMinHeap:
    def test_when_succeeds(self) -> None:
        heap: MinHeap[int] = MinHeap()
        assert heap.peek() is None
        heap.add(125)
        assert heap.peek() == 125
        heap.add(50)
        assert heap.peek() == 50
        heap.add(75)
        assert heap.peek() == 50
        heap.add(25)
        assert heap.peek() == 25
        heap.add(100)
        assert heap.peek() == 25
        heap.add(99)
        assert heap.peek() == 25
        heap.add(99)
        assert heap.peek() == 25
        assert heap.remove() == 25
        assert heap.peek() == 50
        assert heap.remove() == 50
        assert heap.peek() == 75
        assert heap.remove() == 75
        assert heap.peek() == 99
        assert heap.remove() == 99
        assert heap.peek() == 99
        assert heap.remove() == 99
        assert heap.peek() == 100
        assert heap.remove() == 100
        assert heap.peek() == 125
        assert heap.remove() == 125
        assert heap.peek() is None
        heap.add(0)
        assert heap.peek() == 0
        assert heap.remove() == 0
        assert heap.peek() is None

    def test_when_raises_runtime_error(self) -> None:
        heap: MinHeap[int] = MinHeap()
        with pytest.raises(RuntimeError, match="empty"):
            heap.remove()
