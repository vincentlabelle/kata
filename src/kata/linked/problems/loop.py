from kata.linked.structures.snode import SNode


def loop(head: SNode[int]) -> SNode[int] | None:
    """Given a linked list which might contain a loop, return the node at the
    beginning of the loop (if one exists).

    The algorithm must run in O(n) time.

    Parameters
    ----------
    head : SNode[int]
        The head of the linked list.

    Returns
    -------
    SNode[int] | None
        The node at the beginning of the loop if one exists, else `None`.
    """
    set_ = set()
    current: SNode[int] | None = head
    while current is not None:
        if id(current) in set_:
            return current
        set_.add(id(current))
        current = current.next
    return None
