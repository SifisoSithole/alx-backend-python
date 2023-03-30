#!/usr/bin/env python3
"""
This module contains the sum_list function
"""
from typing import List

floatList = List[float]


def sum_list(input_list: floatList) -> float:
    """
    returns the sum of input_list

    args:
        input_list (floatList): list of floats

    return:
        float: sum of input_list
    """

    return sum(input_list)
