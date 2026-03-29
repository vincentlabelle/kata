import pytest

from kata.hash.structures.hash import HashMap


class TestHashMapInit:
    def test_when_succeeds(self) -> None:
        HashMap(1)

    @pytest.mark.parametrize("capacity", [-1, 0])
    def test_when_raises_value_error(self, capacity: int) -> None:
        with pytest.raises(ValueError):
            HashMap(capacity)


class TestHashMapGetItem:
    def test_when_succeeds_without_collision(self) -> None:
        hmap: HashMap[str, int] = HashMap(1)
        hmap["a"] = 0
        assert hmap["a"] == 0

    def test_when_succeeds_with_collision(self) -> None:
        hmap: HashMap[str, int] = HashMap(1)
        hmap["a"] = 0
        hmap["b"] = 1
        assert hmap["b"] == 1

    def test_when_raises_key_error_without_collision(self) -> None:
        hmap: HashMap[str, int] = HashMap(1)
        with pytest.raises(KeyError):
            _ = hmap["a"]

    def test_when_raises_key_error_with_collision(self) -> None:
        hmap: HashMap[str, int] = HashMap(1)
        hmap["a"] = 0
        hmap["b"] = 1
        with pytest.raises(KeyError):
            _ = hmap["c"]


class TestHashMapSetItem:
    def test_when_exist_without_collision(self) -> None:
        hmap: HashMap[str, int] = HashMap(1)
        hmap["a"] = 0
        hmap["a"] = 1
        assert hmap["a"] == 1

    def test_when_exist_with_collision(self) -> None:
        hmap: HashMap[str, int] = HashMap(1)
        hmap["a"] = 0
        hmap["b"] = 1
        hmap["b"] = 2
        assert hmap["b"] == 2

    def test_when_does_not_exist_without_collision(self) -> None:
        hmap: HashMap[str, int] = HashMap(1)
        hmap["a"] = 0
        assert hmap["a"] == 0

    def test_when_does_not_exist_with_collision(self) -> None:
        hmap: HashMap[str, int] = HashMap(1)
        hmap["a"] = 0
        hmap["b"] = 1
        assert hmap["b"] == 1


class TestHashMapDelItem:
    def test_when_succeeds_without_collision(self) -> None:
        hmap: HashMap[str, int] = HashMap(1)
        hmap["a"] = 0
        del hmap["a"]
        assert "a" not in hmap

    def test_when_succeeds_with_collision(self) -> None:
        hmap: HashMap[str, int] = HashMap(1)
        hmap["a"] = 0
        hmap["b"] = 1
        del hmap["b"]
        assert "a" in hmap
        assert "b" not in hmap

    def test_when_raises_key_error_without_collision(self) -> None:
        hmap: HashMap[str, int] = HashMap(1)
        with pytest.raises(KeyError):
            del hmap["a"]

    def test_when_raises_key_error_with_collision(self) -> None:
        hmap: HashMap[str, int] = HashMap(1)
        hmap["a"] = 0
        hmap["b"] = 1
        with pytest.raises(KeyError):
            del hmap["c"]


class TestHashMapLen:
    def test(self) -> None:
        len_ = 0
        hmap: HashMap[int, int] = HashMap(2)
        assert len(hmap) == len_

        # Add
        for i in range(10):
            hmap[i] = 0
            len_ += 1
            assert len(hmap) == len_

        # Delete
        for i in range(10):
            del hmap[i]
            len_ -= 1
            assert len(hmap) == len_

        # Update
        hmap[0] = 0
        hmap[0] = 1
        assert len(hmap) == 1


class TestHashMapIter:
    @pytest.mark.parametrize(
        "pairs",
        [
            [("a", 0)],
            [("a", 0), ("b", 1)],
            [("a", 0), ("b", 1), ("c", 2)],
        ],
    )
    def test(self, pairs: list[tuple[str, int]]) -> None:
        hmap: HashMap[str, int] = HashMap(len(pairs))
        for k, v in pairs:
            hmap[k] = v
        assert set(hmap.items()) == set(pairs)


class TestHashMapEq:
    @pytest.mark.parametrize(
        "pairs, opairs, expected",
        [
            ([], [], True),
            ([("a", 0), ("b", 1)], [("b", 1), ("a", 0)], True),
            ([("a", 0), ("b", 1)], [("a", 0), ("b", 1), ("c", 2)], False),
            ([("a", 0), ("b", 1)], [("a", 0), ("b", 2)], False),
            ([("a", 0), ("b", 1)], [("a", 0), ("c", 1)], False),
        ],
    )
    def test_when_same_type(
        self,
        pairs: list[tuple[str, int]],
        opairs: list[tuple[str, int]],
        expected: bool,
    ) -> None:
        hmap: HashMap[str, int] = HashMap(1)
        for k, v in pairs:
            hmap[k] = v

        other: HashMap[str, int] = HashMap(1)
        for k, v in opairs:
            other[k] = v

        actual = hmap == other
        assert actual == expected

    def test_when_different_type(self) -> None:
        hmap: HashMap[str, int] = HashMap(1)
        assert hmap != "a"


class TestHashMapStr:
    def test_when_empty(self) -> None:
        hmap: HashMap[str, int] = HashMap(1)
        assert str(hmap) == "{}"

    def test_when_non_empty(self) -> None:
        hmap: HashMap[str, int] = HashMap(1)
        hmap["a"] = 0
        hmap["b"] = 1
        assert str(hmap) == "{a: 0, b: 1}"


class TestHashMapRepr:
    def test(self) -> None:
        hmap: HashMap[str, int] = HashMap(1)
        hmap["a"] = 0
        hmap["b"] = 1
        assert repr(hmap) == f"{hmap.__class__.__name__}({hmap})"
