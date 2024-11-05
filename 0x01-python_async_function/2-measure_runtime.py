#!/usr/bin/env python3
"""
Asynchronous Python function to measure the average execution time of a coroutine.
"""
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Calculates the average time taken to execute the `wait_n` function."""
    start_time = time.time()  # Record the start time
    asyncio.run(wait_n(n, max_delay))  # Run the asynchronous function
    total_time = time.time() - start_time  # Compute the total time elapsed
    return total_time / n  # Return the average time per coroutine call
