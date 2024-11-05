#!/usr/bin/env python3
"""Asynchronous Python function that gathers and
   sorts the results of multiple coroutines.
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns a sorted list of delays collected from
       calling `wait_random` n times."""
    results = await asyncio.gather(
        *[wait_random(max_delay) for _ in range(n)]
    )
    return sorted(results)
