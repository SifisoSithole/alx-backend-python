#!/usr/bin/env python3
"""
This module contains the to_kv function
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    returns `k` and `v` as a tuple

    args:
        k (str): 1st element of the tuple
        v (int/float): 2nd element of the tuple

    return:
        tuple: `k` and `v` as a tuple
    """
    return (k, v)
