from kata.stack.structures.stack import Stack


class Queue[T]:
    """Implementation of a queue of `T` with two stacks."""

    def __init__(self) -> None:
        self._enqueue: Stack[T] = Stack()
        self._deque: Stack[T] = Stack()

    def enqueue(self, value: T) -> None:
        """Enqueue `value` onto the queue. The time complexity of this operation
        is O(1).

        Parameters
        ----------
        value : T
            Value to enqueue onto the queue.
        """
        self._enqueue.push(value)

    def peek(self) -> T | None:
        """Peek at the value which is currently at the end of the queue. The
        time complexity of this operation is O(n).

        Returns
        -------
        T | None
            The value at the end of the queue or `None` if the queue is empty.
        """
        self._move()
        return self._deque.peek()

    def _move(self) -> None:
        if self._deque.peek() is None:
            while self._enqueue.peek() is not None:
                self._deque.push(self._enqueue.pop())

    def deque(self) -> T:
        """Deque from the queue. The time complexity of this operation is O(n).

        Raises
        ------
        RuntimeError
            Raised when the queue is empty.

        Returns
        -------
        T
            Dequeued value.
        """
        self._move()
        return self._deque.pop()
