from typing import Self


class BNode[T]:
    """Representation of a node in a binary tree.

    Parameters
    ----------
    value : T
        Value of the node.
    left : Self | None
        Left child of the node, defaults to `None`.
    right : Self | None
        Right child of the node, defaults to `None`.
    """

    _SPLIT = "\u251c "
    _SPLIT_INDENT = "\u2502 "
    _TURN = "\u2514 "
    _TURN_INDENT = "  "

    def __init__(
        self,
        value: T,
        *,
        left: Self | None = None,
        right: Self | None = None,
    ) -> None:
        self.value = value
        self.left = left
        self.right = right

    def __eq__(self, other: object, /) -> bool:
        if not isinstance(other, self.__class__):
            return NotImplemented
        return (
            self.value == other.value
            and self.left == other.left
            and self.right == other.right
        )

    def __str__(self) -> str:
        str_ = self._str(indent="")
        return str_[:-1]

    def _str(self, *, indent: str) -> str:
        s = f"{self.value}\n"
        if self.left is not None and self.right is not None:
            s += self.left.__str(
                indent,
                pre=self._SPLIT,
                new=self._SPLIT_INDENT,
            )
            s += self.right.__str(
                indent,
                pre=self._TURN,
                new=self._TURN_INDENT,
            )
        elif self.left is not None or self.right is not None:
            node: Self = self.left or self.right  # type: ignore[assignment]
            s += node.__str(
                indent,
                pre=self._TURN,
                new=self._TURN_INDENT,
            )
        return s

    def __str(
        self,
        indent: str,
        *,
        pre: str,
        new: str,
    ) -> str:
        return f"{indent}{pre}{self._str(indent=indent + new)}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(\n{self}\n)"
