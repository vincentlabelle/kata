from kata.linked.structures.snode import SNode


def partition(head: SNode[int], value: int) -> None:
    """Partition a linked list around `value`, such that all nodes less than
    `value` come before all nodes greater than equal to `value`. The nodes do
    not have to be sorted.

    The algorithm must run in O(n) time.

    Parameters
    ----------
    head : SNode[int]
        The head of the linked list to partition.
    value : int
        The value around which to partition.
    """
    upper = _find_upper(head, value)
    lower = upper
    while upper is not None and lower is not None:
        upper = _find_upper(upper, value)
        lower = _find_lower(lower, value)
        _swap(upper, lower)


def _find_upper(node: SNode[int] | None, value: int) -> SNode[int] | None:
    current = node
    while current is not None and current.value < value:
        current = current.next
    return current


def _find_lower(node: SNode[int] | None, value: int) -> SNode[int] | None:
    current = node
    while current is not None and current.value >= value:
        current = current.next
    return current


def _swap(upper: SNode[int] | None, lower: SNode[int] | None) -> None:
    if upper is not None and lower is not None:
        lower.value, upper.value = upper.value, lower.value
