#!/usr/bin/env python3
"""
A module containing a coroutine called async_comprehension that collects
10 random numbers using async comprehensions over async_generator.
"""

import typing

# Importing async_generator from the previous task
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    """
    Coroutine that collects 10 random numbers from async_generator using
    an async comprehension and returns them.
    """
    return [rand async for rand in async_generator()]
