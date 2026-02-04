import pytest

from kata.stack.problems.sort import sort
from kata.stack.structures.stack import Stack


class TestSort:
    @pytest.fixture(scope="function")
    def expected(self) -> Stack[int]:
        stack: Stack[int] = Stack()
        stack.push(3)
        stack.push(2)
        stack.push(1)
        return stack

    def test_when_empty(self) -> None:
        stack: Stack[int] = Stack()
        sort(stack)
        assert stack == Stack()

    def test_when_sorted(self, expected: Stack[int]) -> None:
        stack: Stack[int] = Stack()
        stack.push(3)
        stack.push(2)
        stack.push(1)
        sort(stack)
        assert stack == expected

    def test_when_reverse_sorted(self, expected: Stack[int]) -> None:
        stack: Stack[int] = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        sort(stack)
        assert stack == expected

    def test_when_mixed(self, expected: Stack[int]) -> None:
        stack: Stack[int] = Stack()
        stack.push(2)
        stack.push(3)
        stack.push(1)
        sort(stack)
        assert stack == expected
