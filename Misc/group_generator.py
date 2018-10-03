import itertools


def group_generator(n, iterable):
    """Group Generator
    This generator slices the input `iterable` and yield smaller chunks of
    size `n`

    Args:
        n (int): Size of tuple to be yield
        iterable (iterable): An iterable to be sliced

    Yields:
        tuple: A tuple that has size `n`

    Examples:
        >>> iter = range(17)
        >>> for slice in group_generator(n=4, iterable=iter):
        ...     print(slice)
        ...
        (0, 1, 2, 3)
        (4, 5, 6, 7)
        (8, 9, 10, 11)
        (12, 13, 14, 15)
        (16,)
        """
    it = iter(iterable)
    while True:
        chunk = tuple(itertools.islice(it, n))
        if not chunk:
            return
        yield chunk
