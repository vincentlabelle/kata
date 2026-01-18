def urlify(array: list[str], count: int) -> None:
    """Given an array of `count` significant characters replace each space
    character by the three characters: `"%"`, `"2"` and `"0"`.

    The array has extraneous characters at the end to provide space for the
    replacements. The value of these characters is irrelevant.

    As an example, the following inputs:

    `["M", "r", " ", "J", "o", "n", "h", " ", " "]`, and `7`

    yields the following output:

    `["M", "r", "%", "2", "0", "J", "o", "n", "h"]`.

    The algorithm must run in O(n) time and O(1) space.

    Parameters
    ----------
    array : list[str]
        The array for which to perform replacements.
    count : int
        The "true" number of characters within `array` (i.e., excluding the
        extraneous characters).

    Raises
    ------
    ValueError
        Raised when `count` isn't between 0 and `len(array)`.
    """
    _raise_if_count_out_of_bounds(array, count)
    _urlify(array, count)


def _raise_if_count_out_of_bounds(array: list[str], count: int) -> None:
    if not 0 <= count <= len(array):
        message = "cannot urlify; count must between 0 and len(array)"
        raise ValueError(message)


def _urlify(array: list[str], count: int) -> None:
    new = len(array) - 1
    for prev in range(count - 1, -1, -1):
        if array[prev] == " ":
            for char in "02%":
                array[new] = char
                new -= 1
        else:
            array[new] = array[prev]
            new -= 1
