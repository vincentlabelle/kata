from kata.linked.structures.snode import SNode


def sum_lists(one: SNode[int], two: SNode[int]) -> SNode[int]:
    """Given two numbers represented by a linked list where each node contains
    a single digit, add the two numbers and return the sum as a linked list.
    The digits are stored in reverse order.

    As an example, the linked list 7 -> 1 -> 6 represents the number 617.

    The algorithm must run in O(n) where n is the length of the longest linked
    list.

    Parameters
    ----------
    one : SNode[int]
        The head of the list representing the first number.
    two : SNode[int]
        The head of the list representing the second number.

    Returns
    -------
    SNode[int]
        The head of the list representing the sum.
    """
    one_: SNode[int] | None = one
    two_: SNode[int] | None = two
    head = SNode(0)
    sum_ = head
    while one_ is not None or two_ is not None:
        if one_ is not None:
            sum_.value += one_.value
            one_ = one_.next
        if two_ is not None:
            sum_.value += two_.value
            two_ = two_.next
        if one_ is not None or two_ is not None or sum_.value >= 10:
            sum_.next = SNode(sum_.value // 10)
            sum_.value %= 10
            sum_ = sum_.next
    return head
