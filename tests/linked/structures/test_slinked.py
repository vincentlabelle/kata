import pytest

from kata.linked.structures.slinked import SLinked

_VALUES = [0, 1, 2]


@pytest.fixture(scope="function")
def linked() -> SLinked[int]:
    linked: SLinked[int] = SLinked()
    for value in _VALUES:
        linked.append(value)
    return linked


@pytest.fixture(scope="function")
def empty() -> SLinked[int]:
    return SLinked()


class TestSLinkedReverse:
    def test_when_empty(self, empty: SLinked[int]) -> None:
        expected: SLinked[int] = SLinked()
        empty.reverse()
        assert empty == expected

    def test_when_one(self) -> None:
        expected: SLinked[int] = SLinked()
        expected.append(0)

        linked: SLinked[int] = SLinked()
        linked.append(0)
        linked.reverse()

        assert linked == expected

    def test_when_many(self, linked: SLinked[int]) -> None:
        expected: SLinked[int] = SLinked()
        for values in _VALUES:
            expected.prepend(values)

        linked.reverse()

        assert linked == expected


class TestSLinkedInsert:
    def test_when_succeeds(self) -> None:
        expected: SLinked[int] = SLinked()
        expected.prepend(3)
        expected.prepend(2)
        expected.prepend(1)
        expected.prepend(0)

        actual: SLinked[int] = SLinked()
        actual.insert(0, 1)
        actual.insert(1, 3)
        actual.insert(0, 0)
        actual.insert(2, 2)

        assert actual == expected

    @pytest.mark.parametrize("index", [-1, 1])
    def test_when_empty_and_raises_index_error(
        self,
        empty: SLinked[int],
        index: int,
    ) -> None:
        with pytest.raises(IndexError):
            empty.insert(index, 0)

    @pytest.mark.parametrize("index", [-1, len(_VALUES) + 1])
    def test_when_non_empty_and_raises_index_error(
        self,
        linked: SLinked[int],
        index: int,
    ) -> None:
        with pytest.raises(IndexError):
            linked.insert(index, 1)


class TestSLinkedPrependAppend:
    def test(self) -> None:
        expected: SLinked[int] = SLinked()
        expected.append(1)
        expected.append(0)

        actual: SLinked[int] = SLinked()
        actual.prepend(0)
        actual.prepend(1)

        assert actual == expected


class TestSLinkedGetItem:
    def test_when_succeeds(self, linked: SLinked[int]) -> None:
        for i, value in enumerate(linked):
            assert linked[i] == value

    @pytest.mark.parametrize("index", [-1, 0, 1])
    def test_when_empty_and_raises_index_error(
        self,
        empty: SLinked[int],
        index: int,
    ) -> None:
        with pytest.raises(IndexError):
            empty[index]

    @pytest.mark.parametrize("index", [-1, len(_VALUES)])
    def test_when_non_empty_and_raises_index_error(
        self,
        linked: SLinked[int],
        index: int,
    ) -> None:
        with pytest.raises(IndexError):
            linked[index]


class TestSLinkedSetItem:
    @pytest.mark.parametrize("index", range(len(_VALUES)))
    def test_when_succeeds(self, linked: SLinked[int], index: int) -> None:
        linked[index] = -1
        assert linked[index] == -1

    @pytest.mark.parametrize("index", [-1, 0, 1])
    def test_when_empty_and_raises_index_error(
        self,
        empty: SLinked[int],
        index: int,
    ) -> None:
        with pytest.raises(IndexError):
            empty[index] = 0

    @pytest.mark.parametrize("index", [-1, len(_VALUES)])
    def test_when_non_empty_and_raises_index_error(
        self,
        linked: SLinked[int],
        index: int,
    ) -> None:
        with pytest.raises(IndexError):
            linked[index] = 0


class TestSLinkedDelItem:
    def test_when_one(self) -> None:
        linked: SLinked[int] = SLinked()
        linked.append(0)
        del linked[0]
        assert len(linked) == 0

    @pytest.mark.parametrize("index", range(len(_VALUES)))
    def test_when_many(self, linked: SLinked[int], index: int) -> None:
        expected: SLinked[int] = SLinked()
        for i, value in enumerate(linked):
            if i != index:
                expected.append(value)

        del linked[index]

        assert linked == expected

    @pytest.mark.parametrize("index", [-1, 0, 1])
    def test_when_empty_and_raises_index_error(
        self,
        empty: SLinked[int],
        index: int,
    ) -> None:
        with pytest.raises(IndexError):
            del empty[index]

    @pytest.mark.parametrize("index", [-1, len(_VALUES)])
    def test_when_non_empty_and_raises_index_error(
        self,
        linked: SLinked[int],
        index: int,
    ) -> None:
        with pytest.raises(IndexError):
            del linked[index]


class TestSLinkedLen:
    def test(self) -> None:
        linked: SLinked[int] = SLinked()
        assert len(linked) == 0
        linked.append(0)
        assert len(linked) == 1
        del linked[0]
        assert len(linked) == 0
        linked.prepend(0)
        assert len(linked) == 1
        linked.insert(0, 0)
        assert len(linked) == 2
        del linked[0]
        assert len(linked) == 1
        del linked[0]
        assert len(linked) == 0


class TestSLinkedContains:
    def test_when_contains(self, linked: SLinked[int]) -> None:
        for value in _VALUES:
            assert value in linked

    def test_when_empty_and_does_not_contain(
        self,
        empty: SLinked[int],
    ) -> None:
        assert -1 not in empty

    def test_when_non_empty_and_does_not_contain(
        self,
        linked: SLinked[int],
    ) -> None:
        assert -1 not in linked


class TestSLinkedIter:
    def test_when_empty(self, empty: SLinked[int]) -> None:
        assert list(iter(empty)) == []

    def test_when_non_empty(self, linked: SLinked[int]) -> None:
        assert list(iter(linked)) == _VALUES


class TestSLinkedEq:
    @pytest.mark.parametrize("values", [(), (1, 2)])
    def test_when_equal(self, values: tuple[int, ...]) -> None:
        linked: SLinked[int] = SLinked()
        for value in values:
            linked.append(value)

        other: SLinked[int] = SLinked()
        for value in values:
            other.append(value)

        assert other == linked

    @pytest.mark.parametrize(
        "linked_values, other_values",
        [
            ([], [1]),
            ([1, 2], [1, 3]),
        ],
    )
    def test_when_different_head(
        self,
        linked_values: list[int],
        other_values: list[int],
    ) -> None:
        linked: SLinked[int] = SLinked()
        for value in linked_values:
            linked.append(value)

        other: SLinked[int] = SLinked()
        for value in other_values:
            other.append(value)

        assert other != linked

    def test_when_different_type(self, linked: SLinked[int]) -> None:
        assert linked != "a"


class TestSLinkedStr:
    def test_when_empty(self, empty: SLinked[int]) -> None:
        assert str(empty) == "||"

    def test_when_non_empty(self, linked: SLinked[int]) -> None:
        assert str(linked) == f"|{linked._head}|"


class TestSLinkedRepr:
    def test(self, linked: SLinked[int]) -> None:
        assert repr(linked) == f"{linked.__class__.__name__}({linked})"
