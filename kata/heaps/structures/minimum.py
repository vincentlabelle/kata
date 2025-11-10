class MinHeap[T]:
    """Representation of a minimum heap of `T`."""

    def __init__(self) -> None:
        self._values: list[T] = []

    def add(self, value: T) -> None:
        """Add `value` to this heap. The time complexity of this operation is
        O(log(n)).

        Parameters
        ----------
        value : T
            Value to add.

        Raises
        ------
        TypeError
            Raised when `T` doesn't support the `<` operator.
        """
        self._values.append(value)
        self._up(len(self._values) - 1)

    def _up(self, index: int) -> None:
        if index <= 0:
            return
        parent = self._get_parent(index)
        if self._values[index] < self._values[parent]:  # type: ignore[operator]
            self._swap(index, parent)
            self._up(parent)

    @staticmethod
    def _get_parent(index: int) -> int:
        return (index - 1) // 2

    def _swap(self, one: int, two: int) -> None:
        self._values[one], self._values[two] = (
            self._values[two],
            self._values[one],
        )

    def peek(self) -> T | None:
        """Peek at the value which is at the top of the heap. The time
        complexity of this operation is O(1).

        Returns
        -------
        T | None
            The value at the top of the heap or `None` if the heap is empty.
        """
        if len(self._values) == 0:
            return None
        return self._values[0]

    def remove(self) -> T:
        """Remove the value at the top of the heap. The time complexity of this
        operation is O(log(n)).

        Raises
        ------
        RuntimeError
            Raised when the heap is empty.
        TypeError
            Raised when `T` doesn't support the `<` operator.

        Returns
        -------
        T
            The removed value.
        """
        self._raise_if_empty()
        return self._remove()

    def _raise_if_empty(self) -> None:
        if len(self._values) == 0:
            message = "cannot remove from heap; heap is empty"
            raise RuntimeError(message)

    def _remove(self) -> T:
        self._swap(0, len(self._values) - 1)
        value = self._values.pop()
        self._down(0)
        return value

    def _down(self, index: int) -> None:
        min_ = self._get_minimum_child(index)
        if min_ >= len(self._values):
            return
        if self._values[min_] < self._values[index]:  # type: ignore[operator]
            self._swap(index, min_)
            self._down(min_)

    def _get_minimum_child(self, index: int) -> int:
        l, r = 2 * index + 1, 2 * index + 2  # noqa: E741
        if r >= len(self._values) or self._values[l] <= self._values[r]:  # type: ignore[operator]
            return l
        return r

    def __eq__(self, other: object, /) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._values == other._values

    def __str__(self) -> str:
        return str(self._values)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self})"
