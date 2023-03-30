#!/usr/bin/env python3
"""
This module contains the sum_mixed_list
"""
from typing import List, Union

MixedList = List[Union[int, float]]


def sum_mixed_list(mxd_lst: MixedList) -> float:
    """
    returns the sum of mxd_lst

    args:
        mxd_lst (MixedList): list of integers and floats

    return:
        float: sum of mxd_lst
    """
    return sum(mxd_lst)
