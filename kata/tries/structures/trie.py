from kata.tries.structures.tnode import TNode


class Trie:
    """Representation of a trie."""

    _FLAG = "*"

    def __init__(self) -> None:
        self._root = TNode()

    def add(self, word: str) -> None:
        """Add `word` to this trie. The time complexity of this operation is
        O(k), where k is the length of `word`.

        Parameters
        ----------
        word : str
            Word to add.
        """
        node: TNode | None = self._root
        for char in word:
            assert node is not None  # noqa: S101
            if char not in node:
                node[char] = TNode()
            node = node[char]
        assert node is not None  # noqa: S101
        node[self._FLAG] = None

    def complete(self, prefix: str) -> tuple[str, ...]:
        """Find the suffixes which once combined with `prefix` form a word.

        The time complexity of this operation is O(k + m), where k is the length
        of `prefix` and m is the number of nodes in the subtrie of suffixes.

        Parameters
        ----------
        prefix : str
            Prefix for which to find the suffixes.

        Returns
        -------
        tuple[str, ...]
            The suffixes.
        """
        node = self._search(prefix)
        if node is None:
            return ()
        return self._collect(node)

    def _search(self, prefix: str) -> TNode | None:
        # The time complexity of this operation is O(k) where k is the length
        # of `prefix`
        node: TNode | None = self._root
        for char in prefix:
            assert node is not None  # noqa: S101
            if char not in node:
                return None
            node = node[char]
        return node

    def _collect(self, node: TNode) -> tuple[str, ...]:
        # The time complexity of this operation is O(n)
        suffixes: list[str] = []
        self.__collect(node, suffixes)
        return tuple(suffixes)

    def __collect(
        self,
        node: TNode,
        suffixes: list[str],
        suffix: str = "",
    ) -> None:
        for char, child in node.items():
            if char == self._FLAG:
                suffixes.append(suffix)
            else:
                assert child is not None  # noqa: S101
                self.__collect(child, suffixes, suffix + char)

    def __eq__(self, other: object, /) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return self._root == other._root

    def __str__(self) -> str:
        return str(self._root)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self})"
