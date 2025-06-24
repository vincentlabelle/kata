from kata.linked.snode import SNode


class Stack[T]:
    """Representation of a stack of `T`."""

    def __init__(self) -> None:
        self._head: SNode[T] | None = None

    def push(self, value: T) -> None:
        """Push `value` onto the stack. The time complexity of this operation
        is O(1).

        Parameters
        ----------
        value : T
            Value to push onto the stack.
        """
        self._head = SNode(value, self._head)

    def peek(self) -> T | None:
        """Peek at the value which is currently at the top of the stack. The
        time complexity of this operation is O(1).

        Returns
        -------
        T | None
            The value at the top of the stack or `None` if the stack is empty.
        """
        if self._head is None:
            return None
        return self._head.value

    def pop(self) -> T:
        """Pop from the stack. The time complexity of this operation is O(1).

        Raises
        ------
        RuntimeError
            Raised when the stack is empty.

        Returns
        -------
        T
            Popped value.
        """
        self._raise_if_empty()
        return self._pop()

    def _raise_if_empty(self) -> None:
        if self._head is None:
            message = "cannot pop from stack; stack is empty"
            raise RuntimeError(message)

    def _pop(self) -> T:
        head: SNode[T] = self._head  # type: ignore[assignment]
        self._head = head.next
        return head.value
