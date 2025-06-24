import pytest

from kata.linked.stack import Stack


class TestStackPush:
    def test(self) -> None:
        stack: Stack[int] = Stack()
        stack.push(0)
        assert stack.pop() == 0
        stack.push(1)
        stack.push(2)
        assert stack.pop() == 2


class TestStackPeek:
    def test(self) -> None:
        stack: Stack[int] = Stack()
        assert stack.peek() is None
        stack.push(0)
        assert stack.peek() == 0
        stack.push(1)
        stack.push(2)
        assert stack.peek() == 2


class TestStackPop:
    def test_when_succeeds(self) -> None:
        stack: Stack[int] = Stack()
        stack.push(0)
        assert stack.pop() == 0
        assert stack.peek() is None
        stack.push(1)
        stack.push(2)
        assert stack.pop() == 2
        assert stack.peek() == 1
        assert stack.pop() == 1
        assert stack.peek() is None

    def test_when_raises_runtime_error(self) -> None:
        stack: Stack[int] = Stack()
        with pytest.raises(RuntimeError, match="empty"):
            stack.pop()
