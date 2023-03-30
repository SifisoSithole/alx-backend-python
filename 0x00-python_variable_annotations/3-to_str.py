#!/usr/bin/python3
"""
this module contains the to_str function

the to_str function returns the string represantation of a float
"""


def to_str(n: float) -> str:
    """
    returns the string represantation of the float

    arg:
        n (float): float to represent as string

    return:
        str: string represantation of n
    """
    if type(n) is not float:
        raise TypeError('n must be a float')

    return str(n)
