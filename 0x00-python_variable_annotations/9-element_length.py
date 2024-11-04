#!/usr/bin/env python3
'''
type-annotated function that returns a list of tuples
with each element and its length
'''
from typing import List, Tuple, Sequence

def element_length(lst: Sequence[str]) -> List[Tuple[str, int]]:
    '''Takes a sequence of strings and returns a list of tuples
       with each string and its length
    '''
    return [(i, len(i)) for i in lst]
