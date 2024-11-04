#!/usr/bin/env python3
"""
This module contains a type-annotated function `to_kv` that
returns a tuple with a string and the square of an int or float.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple where the first element is the string `k`
       and the second element is the square of `v` as a float."""
    return (k, float(v ** 2))
