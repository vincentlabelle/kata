import pytest

from kata.tries.structures.trie import Trie

_WORDS = ("cat", "catnip", "caterpillar", "cop", "cooler", "cool", "sound")


@pytest.fixture(scope="function")
def trie() -> Trie:
    trie = Trie()
    for word in _WORDS:
        trie.add(word)
    return trie


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
    def test(
        self,
        trie: Trie,
        prefix: str,
        expected: tuple[str, ...],
    ) -> None:
        actual = trie.complete(prefix)
        assert actual == expected


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
