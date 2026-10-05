def binary_to_string(value: float) -> str:
    """Given a real number between 0 and 1 exclusively, produce the binary
    representation.

    If the number cannot be represented accurately in binary with at most 32
    characters, returns `"ERROR"`.

    Parameters
    ----------
    value : float
        The number to represent in binary.

    Returns
    -------
    str
        The binary representation, or `"ERROR"` if either `value` is not
        between 0 and 1 or `value` cannot be represented accurately with
        32 characters.
    """
    if not 0.0 < value < 1.0:
        return "ERROR"
    return _to_string(value)


def _to_string(value: float) -> str:
    v, bits = value, ["0."]
    while v > 0.0:
        if len(bits) >= 33:
            return "ERROR"
        v *= 2.0
        if v >= 1.0:
            bits.append("1")
            v -= 1.0
        else:
            bits.append("0")
    return "".join(bits)
