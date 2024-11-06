#!/usr/bin/env python3
"""
Task 2: Measure Runtime
Import async_comprehension from the previous file and write
a coroutine called measure_runtime that will execute 
async_comprehension four times in parallel using asyncio.gather.
measure_runtime should measure the total runtime and return it.
"""

import asyncio
import time

# Importing async_comprehension from the previous file
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime of running async_comprehension
    four times in parallel.
    """
    start_time = time.time()
    
    # Run async_comprehension four times in parallel
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    
    # Return the time difference
    return time.time() - start_time
