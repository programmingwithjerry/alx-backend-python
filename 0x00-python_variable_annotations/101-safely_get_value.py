#!/usr/bin/env python3
"""
Type-annotated function to safely fetch a value from a dictionary.
"""
from typing import Any, Mapping, Union, TypeVar

T = TypeVar('T')
Res = Union[Any, T]
Def = Union[T, None]

def safely_get_value(dct: Mapping, key: Any, default: Def = None) -> Res:
    """Fetches a value from a dictionary using a given key; returns
       a default value if the key is not present."""
    if key in dct:
        return dct[key]
    else:
        return default
