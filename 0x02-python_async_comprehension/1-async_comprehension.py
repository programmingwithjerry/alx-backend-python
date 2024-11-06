#!/usr/bin/env python3
"""
A module containing a coroutine called async_comprehension that collects
10 random numbers using async comprehensions over async_generator.
"""

from typing import List
# Import the async_generator from the previous task
from async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers from async_generator using
    an async comprehension and returns them.

    Returns:
        List[float]: A list of 10 random float numbers between 0 and 10.
    """
    return [number async for number in async_generator()]
