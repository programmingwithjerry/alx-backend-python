#!/usr/bin/env python3
"""
Type-annotated function that returns a list of tuples
containing each element and its length.
"""
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Takes an iterable of sequences and returns a list of tuples,
       where each tuple includes a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
