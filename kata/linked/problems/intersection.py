from kata.linked.structures.snode import SNode


def intersection(one: SNode[int], two: SNode[int]) -> int | None:
    """Given two linked list, find an intersecting value (i.e., a value which
    is in both list).

    The algorithm must run in O(n + m) time.

    Parameters
    ----------
    one : SNode[int]
        The head of the first linked list.
    two : SNode[int]
        The head of the second linked list.

    Returns
    -------
    int | None
        The intersecting value, or `None` if the list do not intersect.
    """
    set_ = _unique(one)
    return _search(two, set_)


def _unique(one: SNode[int]) -> set[int]:
    set_: set[int] = set()
    current: SNode[int] | None = one
    while current is not None:
        set_.add(current.value)
        current = current.next
    return set_


def _search(two: SNode[int], set_: set[int]) -> int | None:
    current: SNode[int] | None = two
    while current is not None:
        if current.value in set_:
            return current.value
        current = current.next
    return None
