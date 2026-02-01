from kata.linked.structures.snode import SNode


def is_palindrome(head: SNode[str]) -> bool:
    """Given a linked list, verify if it is a palindrome.

    The algorithm must run in O(n) time.

    Parameters
    ----------
    head : SNode[str]
        The head of the list for which to verify.

    Returns
    -------
    bool
        `True` if the list is a palindrome, else `False`.
    """
    array = _to_array(head)
    return array == array[::-1]


def _to_array(head: SNode[str]) -> list[str]:
    array = []
    current: SNode[str] | None = head
    while current is not None:
        array.append(current.value)
        current = current.next
    return array
