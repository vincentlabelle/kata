from kata.linked.structures.snode import SNode


def remove_duplicates(head: SNode[int]) -> None:
    """Given the head of a linked list, remove duplicates from the list.

    The algorithm must run in O(n) time.

    Parameters
    ----------
    head : SNode[int]
        The head of the list for which to remove duplicates.
    """
    seen = {head.value}
    previous, current = head, head.next
    while current is not None:
        if current.value in seen:
            previous.next = current.next
        else:
            seen.add(current.value)
            previous = current
        current = current.next
