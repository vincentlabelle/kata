import pytest

from kata.stacks.structures.stack import Stack


@pytest.fixture
def stack() -> Stack[int]:
    return Stack()


class TestStackPush:
    def test(self, stack: Stack[int]) -> None:
        stack.push(0)
        assert stack.pop() == 0
        stack.push(1)
        stack.push(2)
        assert stack.pop() == 2


class TestStackPeek:
    def test(self, stack: Stack[int]) -> None:
        assert stack.peek() is None
        stack.push(0)
        assert stack.peek() == 0
        stack.push(1)
        stack.push(2)
        assert stack.peek() == 2


class TestStackPop:
    def test_when_succeeds(self, stack: Stack[int]) -> None:
        stack.push(0)
        assert stack.pop() == 0
        assert stack.peek() is None
        stack.push(1)
        stack.push(2)
        assert stack.pop() == 2
        assert stack.peek() == 1
        assert stack.pop() == 1
        assert stack.peek() is None

    def test_when_raises_runtime_error(self, stack: Stack[int]) -> None:
        with pytest.raises(RuntimeError, match="empty"):
            stack.pop()


class TestStackEq:
    @pytest.fixture
    def other(self) -> Stack[int]:
        return Stack()

    @pytest.mark.parametrize("values", [[], [0, 1]])
    def test_when_equal(
        self,
        stack: Stack[int],
        other: Stack[int],
        values: list[int],
    ) -> None:
        for v in values:
            stack.push(v)
            other.push(v)
        assert stack == other

    @pytest.mark.parametrize(
        "stack_values, other_values",
        [
            ([], [1]),
            ([1, 2], [1, 3]),
        ],
    )
    def test_when_different_head(
        self,
        stack: Stack[int],
        other: Stack[int],
        stack_values: list[int],
        other_values: list[int],
    ) -> None:
        for v in stack_values:
            stack.push(v)
        for v in other_values:
            other.push(v)
        assert other != stack

    def test_when_different_type(self, stack: Stack[int]) -> None:
        assert stack != "a"


class TestStackStr:
    @pytest.mark.parametrize(
        "values, expected",
        [
            ([], "||"),
            ([0, 1], "|1->0|"),
        ],
    )
    def test(
        self,
        stack: Stack[int],
        values: list[int],
        expected: str,
    ) -> None:
        for v in values:
            stack.push(v)
        assert str(stack) == expected


class TestStackRepr:
    def test(self, stack: Stack[int]) -> None:
        assert repr(stack) == f"{stack.__class__.__name__}({stack})"
