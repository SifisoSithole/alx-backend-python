#!/usr/bin/env python3
"""
this module cantains the floor function.
The floor function rounds down a float to the nearest integer
"""
import math


def floor(n: float) -> int:
    """
    rounds down n to the nearest integer

    args:
        n (float): float to round down

    return:
        int
    """
    return math.floor(n)
