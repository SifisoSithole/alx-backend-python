#!/usr/bin/env python3
"""
this module contains the element_length function

"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    returns an array of with the length of each element

    arg:
        lst (list): list
    """
    return [(i, len(i)) for i in lst]
