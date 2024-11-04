#!/usr/bin/env python3
"""
This module contains a type-annotated function `sum_mixed_list`
that returns the sum of a list containing integers and floats.
"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a list containing integers and floats."""
    return sum(mxd_lst)
