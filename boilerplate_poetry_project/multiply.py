def multiply_int(x: int, y: int) -> int:
    """Multiply two integers.

    Parameters:
    - x (int): The first integer to multiply.
    - y (int): The second integer to multiply.

    Returns:
    - int: The product of x and y.

    Raises:
    - TypeError: If either x or y is not an integer.

    Example:
    >>> multiply_int(2, 3)
    6
    """
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Both x and y must be integers.")
    return x * y
