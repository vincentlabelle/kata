from kata.linked.structures.snode import SNode


class Queue[T]:
    """Representation of a queue of `T`."""

    def __init__(self) -> None:
        self._head: SNode[T] | None = None
        self._tail: SNode[T] | None = None

    def enqueue(self, value: T) -> None:
        """Enqueue `value` onto the queue. The time complexity of this operation
        is O(1).

        Parameters
        ----------
        value : T
            Value to enqueue onto the queue.
        """
        node = SNode(value)
        if self._tail is None:
            self._head = node
        else:
            self._tail.next = node
        self._tail = node

    def peek(self) -> T | None:
        """Peek at the value which is currently at the end of the queue. The
        time complexity of this operation is O(1).

        Returns
        -------
        T | None
            The value at the end of the queue or `None` if the queue is empty.
        """
        if self._head is None:
            return None
        return self._head.value

    def deque(self) -> T:
        """Deque from the queue. The time complexity of this operation is O(1).

        Raises
        ------
        RuntimeError
            Raised when the queue is empty.

        Returns
        -------
        T
            Dequeued value.
        """
        self._raise_if_is_empty()
        return self._deque()

    def _raise_if_is_empty(self) -> None:
        if self._head is None:
            message = "cannot deque from queue; queue is empty"
            raise RuntimeError(message)

    def _deque(self) -> T:
        head: SNode[T] = self._head  # type: ignore[assignment]
        self._head = head.next
        if self._head is None:
            self._tail = None
        return head.value

    def __eq__(self, other: object, /) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._head == other._head

    def __str__(self) -> str:
        if self._head is None:
            return "||"
        return f"|{self._head}|"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self})"
