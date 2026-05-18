def sorted_merge(one: list[int], two: list[int]) -> None:
    """Given two sorted arrays, when `one` has a large enough buffer at the end
    to hold `two`, merge `two` into `one` in sorted order.

    This algorithm must run in O(n + m) time.

    Parameters
    ----------
    one : list[int]
        First array to merge.
    two : list[int]
        Second array to merge.

    Raises
    ------
    ValueError
        Raised when the length of `two` is greater than the length of `one`.
    """
    _raise_if_two_bigger_than_one(one, two)

    # Determine bounds
    llower, rlower = 0, len(one) - len(two)
    lupper, rupper = rlower - 1, len(one) - 1

    # Copy in new array
    other = _make_copy(one, two, llower, lupper, rlower, rupper)

    # Copy back in `one`
    current, llower, rlower = _copy_compare(
        one,
        other,
        llower,
        lupper,
        rlower,
        rupper,
    )
    _copy_remainder(one, other, current, llower, lupper)
    _copy_remainder(one, other, current, rlower, rupper)


def _raise_if_two_bigger_than_one(one: list[int], two: list[int]) -> None:
    if len(two) > len(one):
        message = (
            "cannot merge; "
            + "the length of one must be equal to or greater than the length "
            + "of two"
        )
        raise ValueError(message)


def _make_copy(
    one: list[int],
    two: list[int],
    llower: int,
    lupper: int,
    rlower: int,
    rupper: int,
) -> list[int]:
    other = [0] * len(one)
    for i in range(llower, lupper + 1):
        other[i] = one[i]
    for i in range(rlower, rupper + 1):
        other[i] = two[i - rlower]
    return other


def _copy_compare(
    one: list[int],
    other: list[int],
    llower: int,
    lupper: int,
    rlower: int,
    rupper: int,
) -> tuple[int, int, int]:
    current = llower
    while llower <= lupper and rlower <= rupper:
        if other[llower] <= other[rlower]:
            one[current] = other[llower]
            llower += 1
        else:
            one[current] = other[rlower]
            rlower += 1
        current += 1
    return current, llower, rlower


def _copy_remainder(
    one: list[int],
    other: list[int],
    current: int,
    lower: int,
    upper: int,
) -> None:
    while lower <= upper:
        one[current] = other[lower]
        lower += 1
        current += 1
