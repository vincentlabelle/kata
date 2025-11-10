import pytest

from kata.heaps.structures.minimum import MinHeap


@pytest.fixture(scope="function")
def heap(values: tuple[int, ...]) -> MinHeap[int]:
    heap: MinHeap[int] = MinHeap()
    for value in values:
        heap.add(value)
    return heap


@pytest.fixture(scope="module")
def values() -> tuple[int, ...]:
    return (2, 1, 0)


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


class TestMinHeapEq:
    def test_when_equal(
        self,
        heap: MinHeap[int],
        values: tuple[int, ...],
    ) -> None:
        other: MinHeap[int] = MinHeap()
        for value in values:
            other.add(value)
        assert other == heap

    def test_when_different_values(
        self,
        heap: MinHeap[int],
        values: tuple[int, ...],
    ) -> None:
        other: MinHeap[int] = MinHeap()
        for value in sorted(values):
            other.add(value)
        assert other != heap

    def test_when_different_type(self, heap: MinHeap[int]) -> None:
        assert heap != "a"


class TestMinHeapStr:
    def test(self, heap: MinHeap[int]) -> None:
        assert str(heap) == str([0, 2, 1])


class TestMinHeapRepr:
    def test(self, heap: MinHeap[int]) -> None:
        assert repr(heap) == f"{heap.__class__.__name__}({heap})"
