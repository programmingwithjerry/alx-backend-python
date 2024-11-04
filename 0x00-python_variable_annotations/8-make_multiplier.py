#!/usr/bin/env python3
"""
This module contains a type-annotated function `make_multiplier` that
returns a function to multiply a float by a given multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''multiplier float uses callable from typing
    '''
    return lambda x: x * multiplier
