import pytest

from kata.trie.structures.trie import Trie

_WORDS = ("cat", "catnip", "caterpillar", "cop", "cooler", "cool", "sound")


@pytest.fixture(scope="function")
def trie() -> Trie:
    trie = Trie()
    for word in _WORDS:
        trie.add(word)
    return trie


class TestTrieAdd:
    @pytest.mark.parametrize(
        "words",
        [
            ("a",),
            ("ab",),
            ("a", "ab"),
            ("ab", "a"),
        ],
    )
    def test_when_succeeds(self, trie: Trie, words: tuple[str, ...]) -> None:
        for word in words:
            trie.add(word)
        actual = trie.complete(words[-1])
        assert "" in actual

    def test_when_raises_value_error(self, trie: Trie) -> None:
        with pytest.raises(ValueError):
            trie.add("")


class TestTrieComplete:
    @pytest.mark.parametrize(
        "prefix, expected",
        [
            ("", _WORDS),
            ("s", ("ound",)),
            ("coo", ("ler", "l")),
            ("cool", ("er", "")),
            ("cop", ("",)),
            ("z", ()),
        ],
    )
    def test_when_non_empty(
        self,
        trie: Trie,
        prefix: str,
        expected: tuple[str, ...],
    ) -> None:
        actual = trie.complete(prefix)
        assert actual == expected

    @pytest.mark.parametrize("prefix", ["", "z"])
    def test_when_empty(self, prefix: str) -> None:
        trie = Trie()
        actual = trie.complete(prefix)
        assert len(actual) == 0


class TestTrieEq:
    def test_when_equal(self, trie: Trie) -> None:
        other = Trie()
        for word in _WORDS:
            other.add(word)
        assert other == trie

    def test_when_different_root(self, trie: Trie) -> None:
        other = Trie()
        for word in _WORDS[:-1]:
            other.add(word)
        assert other != trie

    def test_when_different_type(self, trie: Trie) -> None:
        assert trie != "a"


class TestTrieRepr:
    def test(self, trie: Trie) -> None:
        assert repr(trie) == f"{trie.__class__.__name__}({trie})"
