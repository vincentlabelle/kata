def pairwise_swap(value: int) -> int:
    """Swap odd and even bits in an unsigned integer representable with 32 bits.

    Parameters
    ----------
    value : int
        Integer for which to swap the bits.

    Raises
    ------
    ValueError
        Raised when `value` cannot be represented with 32 bits.

    Returns
    -------
    int
        The integer with bits swapped.
    """
    _raise_if_too_many_bits(value)
    return ((value & 0x55555555) << 1) | ((value & 0xAAAAAAAA) >> 1)


def _raise_if_too_many_bits(value: int) -> None:
    if value < 0 or value > 0xFFFFFFFF:
        message = "cannot swap; value must be representable in 32 bits"
        raise ValueError(message)
