from typing import Iterable

from kata.graph.structures.vertex import Vertex


def build_order(
    projects: list[str],
    dependencies: list[tuple[str, str]],
) -> list[str]:
    """Given a list of projects and a list of dependencies, find a build order
    that will allow the projects to be built.

    The algorithm must run in O(P + D) where P is the number of projects and
    D is the number of dependencies.

    Parameters
    ----------
    projects : list[str]
        The projects to build.
    dependencies : list[tuple[str, str]]
        The dependencies between project; for each dependency, the second
        project is dependent on the first project (i.e., the first project must
        be built first).

    Raises
    ------
    ValueError
        Raised if `projects` and `dependencies` are inconsistent (e.g., a
        project listed in `dependencies` is not in `projects), or
        if there is a circular dependency between projects.

    Returns
    -------
    list[str]
        The build order.
    """
    dependencies_ = _map(dependencies)
    graph = _make(projects, dependencies_)
    return _traverse(graph)


def _map(
    dependencies: list[tuple[str, str]],
) -> dict[str, list[str]]:
    map_: dict[str, list[str]] = {}
    for dependency in dependencies:
        dependee, depender = dependency
        map_[depender] = map_.get(depender, [])
        map_[depender].append(dependee)
    return map_


def _make(
    projects: list[str],
    dependencies: dict[str, list[str]],
) -> Iterable[Vertex[str]]:
    graph = {p: Vertex(p) for p in projects}
    for depender, dependees in dependencies.items():
        _raise_if_missing(graph, depender)
        for dependee in dependees:
            _raise_if_missing(graph, dependee)
            graph[depender].adjacents.append(graph[dependee])
    return graph.values()


def _raise_if_missing(graph: dict[str, Vertex[str]], project: str) -> None:
    if project not in graph:
        message = "cannot build; projects and dependencies are inconsistent"
        raise ValueError(message)


def _traverse(graph: Iterable[Vertex[str]]) -> list[str]:
    traversed: list[str] = []
    seen: set[Vertex[str]] = set()
    for vertex in graph:
        if vertex not in seen:
            __traverse(vertex, traversed, seen, set())
    return traversed


def __traverse(
    vertex: Vertex[str],
    traversed: list[str],
    seen: set[Vertex[str]],
    check: set[Vertex[str]],
) -> None:
    seen.add(vertex)
    check.add(vertex)
    for adjacent in vertex.adjacents:
        _raise_if_checked(adjacent, check)
        if adjacent not in seen:
            __traverse(adjacent, traversed, seen, check)
    check.remove(vertex)
    traversed.append(vertex.value)


def _raise_if_checked(adjacent: Vertex[str], check: set[Vertex[str]]) -> None:
    if adjacent in check:
        message = "cannot build; circular dependency encountered"
        raise ValueError(message)
