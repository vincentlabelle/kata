import pytest

from kata.graph.problems.build_order import build_order


class TestBuildOrder:
    @pytest.mark.parametrize(
        "projects, dependencies, expected",
        [
            (
                [],
                [],
                [],
            ),
            (
                ["a", "b", "c", "d", "e", "f"],
                [],
                ["a", "b", "c", "d", "e", "f"],
            ),
            (
                ["a", "b", "c", "d", "e", "f"],
                [("a", "d"), ("f", "b"), ("b", "d"), ("f", "a"), ("d", "c")],
                ["f", "a", "b", "d", "c", "e"],
            ),
            (
                ["a", "b", "c", "d"],
                [("b", "a"), ("c", "a"), ("d", "b"), ("d", "c")],
                ["d", "b", "c", "a"],
            ),
        ],
    )
    def test_when_succeeds(
        self,
        projects: list[str],
        dependencies: list[tuple[str, str]],
        expected: list[str],
    ) -> None:
        assert build_order(projects, dependencies) == expected

    @pytest.mark.parametrize(
        "projects, dependencies",
        [
            (
                ["a", "b"],
                [("a", "c")],
            ),
            (
                ["a", "b"],
                [("c", "a")],
            ),
        ],
    )
    def test_when_raises_value_error_due_to_inconsistent(
        self,
        projects: list[str],
        dependencies: list[tuple[str, str]],
    ) -> None:
        with pytest.raises(ValueError, match="inconsistent"):
            build_order(projects, dependencies)

    @pytest.mark.parametrize(
        "projects, dependencies",
        [
            (
                ["a", "b"],
                [("a", "b"), ("b", "a")],
            ),
            (
                ["a", "b", "c"],
                [("a", "b"), ("b", "c"), ("c", "a")],
            ),
        ],
    )
    def test_when_raises_value_error_due_to_circle(
        self,
        projects: list[str],
        dependencies: list[tuple[str, str]],
    ) -> None:
        with pytest.raises(ValueError, match="circular"):
            build_order(projects, dependencies)
