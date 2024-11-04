#!/usr/bin/env python3
"""
Type-annotated function that safely retrieves a value from a dictionary.
"""
from typing import Any, TypeVar, Mapping, Optional

T = TypeVar('T')

def safely_get_value(dct: Mapping[Any, T], key: Any, default: Optional[T] = None) -> Optional[T]:
    """Safely gets a value from a dictionary using the provided key; returns
       the default if the key is not found."""
    if key in dct:
        return dct[key]
    else:
        return default
