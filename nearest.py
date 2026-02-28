def nearest_square(num):
    """
    Returns the nearest perfect square to the given number.
    """
    root = 0
    while (root +1) ** 2 < num:
        root += 1
    return root ** 2

