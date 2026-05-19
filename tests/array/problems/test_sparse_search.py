import pytest

from kata.array.problems.sparse_search import sparse_search


class TestSparseSearch:
    @pytest.mark.parametrize(
        "array, value, expected",
        [
            ([], "a", -1),
            ([""], "a", -1),
            (["b"], "a", -1),
            (["b"], "c", -1),
            (["b"], "b", 0),
            (["", "", ""], "a", -1),
            (["b", "c", "d", "e", "g"], "a", -1),
            (["b", "c", "d", "e", "g"], "f", -1),
            (["b", "c", "d", "e", "g"], "h", -1),
            (["b", "c", "d", "e", "g"], "b", 0),
            (["b", "c", "d", "e", "g"], "c", 1),
            (["b", "c", "d", "e", "g"], "d", 2),
            (["b", "c", "d", "e", "g"], "e", 3),
            (["b", "c", "d", "e", "g"], "g", 4),
            (["b", "c", "", "", "e", "f"], "a", -1),
            (["b", "c", "", "", "e", "f"], "d", -1),
            (["b", "c", "", "", "e", "f"], "g", -1),
            (["b", "c", "", "", "e", "f"], "b", 0),
            (["b", "c", "", "", "e", "f"], "c", 1),
            (["b", "c", "", "", "e", "f"], "e", 4),
            (["b", "c", "", "", "e", "f"], "f", 5),
            (["", "b", "", "", "d", ""], "a", -1),
            (["", "b", "", "", "d", ""], "c", -1),
            (["", "b", "", "", "d", ""], "e", -1),
            (["", "b", "", "", "d", ""], "b", 1),
            (["", "b", "", "", "d", ""], "d", 4),
            (["", "", "", "", "d", "f"], "b", -1),
            (["", "", "", "", "d", "f"], "e", -1),
            (["", "", "", "", "d", "f"], "g", -1),
            (["", "", "", "", "e", "f"], "e", 4),
            (["", "", "", "", "e", "f"], "f", 5),
            (["b", "d", "", "", "", ""], "a", -1),
            (["b", "d", "", "", "", ""], "c", -1),
            (["b", "d", "", "", "", ""], "e", -1),
            (["b", "d", "", "", "", ""], "b", 0),
            (["b", "d", "", "", "", ""], "d", 1),
        ],
    )
    def test_when_succeeds(
        self,
        array: list[str],
        value: str,
        expected: int,
    ) -> None:
        assert sparse_search(array, value) == expected

    def test_when_raises_value_error(self) -> None:
        with pytest.raises(ValueError):
            sparse_search([""], "")
