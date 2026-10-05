from kata.stack.structures.stack import Stack


def sort(stack: Stack[int]) -> None:
    """Sort `stack` such that the smallest items are on the top without using
    any other data structures except another stack.

    The algorithm must run in O(n^2) time.

    Parameters
    ----------
    stack : Stack[int]
        Stack to sort.
    """
    reverse = _empty_and_reverse_sort(stack)
    _fill(stack, with_=reverse)


def _empty_and_reverse_sort(stack: Stack[int]) -> Stack[int]:
    reverse: Stack[int] = Stack()
    while stack.peek() is not None:
        value = stack.pop()
        while reverse.peek() is not None and value < reverse.peek():  # type: ignore[operator]
            stack.push(reverse.pop())
        reverse.push(value)
    return reverse


def _fill(stack: Stack[int], with_: Stack[int]) -> None:
    while with_.peek() is not None:
        stack.push(with_.pop())
