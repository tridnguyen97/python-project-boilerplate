def add_int(x: int, y: int) -> int:
    """
    Add two integers.

    Parameters:
    - x (int): The first integer to add.
    - y (int): The second integer to add.

    Returns:
    - int: The sum of x and y.

    Example:
    >>> add_int(2, 3)
    5
    """
    if not all(isinstance(i, int) for i in [x, y]):
        raise TypeError("Both inputs must be integers")
    return x + y
