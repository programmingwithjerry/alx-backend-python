#!/usr/bin/env python3
"""
Asynchronous function that schedules multiple tasks
using `task_wait_random`.
"""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Runs `task_wait_random` n times and
        returns a sorted list of the delays."""
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = await asyncio.gather(*tasks)  # Await all tasks concurrently
    return sorted(results)  # Return the sorted results
