#!/usr/bin/python3
""" module 0-minoperations.py """


def minOperations(n: int) -> int:
    """
    Returns the minimum number of operations needed to result in exactly
     n H characters in a text file.
    Args:
        n: An integer representing the number of Hs to produce.
    Returns:
        An integer representing the minimum number of operations needed
         to produce n Hs, or 0 if n <= 1.
    """
    if n <= 1:
        return 0
    ops = 0
    divisor = 2
    while divisor <= n:
        if n % divisor == 0:
            ops += divisor
            n //= divisor
        else:
            divisor += 1

    return ops
