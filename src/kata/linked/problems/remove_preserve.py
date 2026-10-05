from kata.linked.structures.snode import SNode


def remove_preserve[T](node: SNode[T]) -> None:
    """Remove `node` from the linked list it is a part of while preserving the
    entire remaining list.

    This is a no-op if `node` is the last node of the linked list.

    The algorithm must run in constant time.

    Parameters
    ----------
    node : SNode[T]
        Node to remove.
    """
    if node.next is None:
        return
    node.value = node.next.value
    node.next = node.next.next
