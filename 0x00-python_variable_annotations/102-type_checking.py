#!/usr/bin/env python3
"""
A type-annotated function that generates repeated copies of items in a tuple.
"""
from typing import List, Tuple

def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Produces a list by duplicating each element in a
       tuple based on the given factor."""
    zoomed_in: List = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in

array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
