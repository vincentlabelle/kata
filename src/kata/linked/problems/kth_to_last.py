from kata.linked.structures.snode import SNode


def kth_to_last(head: SNode[int], k: int) -> int | None:
    """Find the kth to last element given the head of a linked list.

    The algorithm must run in O(n) time and O(1) space.

    Parameters
    ----------
    head : SNode[int]
        The head of the list for which to find.
    k : int
        The index of the element starting from the end of the list.

    Returns
    -------
    int | None
        The kth to last element, or `None` if `k` is out of bounds.
    """
    if k < 0:
        return None
    return _kth_to_last(head, k)


def _kth_to_last(head: SNode[int], k: int) -> int | None:
    current: SNode[int] | None = head
    runner = head

    for _ in range(k + 1):
        if current is None:
            return None
        current = current.next

    while current is not None:
        current = current.next
        assert runner.next is not None  # noqa: S101
        runner = runner.next

    return runner.value
