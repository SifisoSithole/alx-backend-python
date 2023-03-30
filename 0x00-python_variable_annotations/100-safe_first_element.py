#!/usr/bin/env python3
"""
this module contains safe_first_element
"""
from typing import Sequence, Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    returns the first element

    """
    if lst:
        return lst[0]
    else:
        return None
