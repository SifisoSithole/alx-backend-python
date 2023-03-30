#!/usr/bin/env python3
"""
This module contains `make_multiple` function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns a function that multiplies a float by multiplier

    arg:
        multiplier (float): multiplier

    return:
       multiply (function): a function that multiplies a float
    """
    def multiply(num: float) -> float:
        return multiplier * num

    return multiply
