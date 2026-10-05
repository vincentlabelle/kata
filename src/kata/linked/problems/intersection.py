from kata.linked.structures.snode import SNode


def intersection(one: SNode[int], two: SNode[int]) -> SNode[int] | None:
    """Given two linked list, determine if the two lists intersect
    (by reference) and return the intersecting node.

    The algorithm must run in O(n + m) time.

    Parameters
    ----------
    one : SNode[int]
        The head of the first linked list.
    two : SNode[int]
        The head of the second linked list.

    Returns
    -------
    SNode[int] | None
        The intersecting node, or `None` if the lists do not intersect.
    """
    set_ = _unique(one)
    return _search(two, set_)


def _unique(one: SNode[int]) -> set[int]:
    set_: set[int] = set()
    current: SNode[int] | None = one
    while current is not None:
        set_.add(id(current))
        current = current.next
    return set_


def _search(two: SNode[int], set_: set[int]) -> SNode[int] | None:
    current: SNode[int] | None = two
    while current is not None:
        if id(current) in set_:
            return current
        current = current.next
    return None
