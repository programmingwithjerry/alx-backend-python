#!/usr/bin/env python3
"""
Asynchronous coroutine that waits for a random
delay between 0 and max_delay seconds.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay between 0 and max_delay
       seconds and returns the delay."""
    delay = random.random() * max_delay
    await asyncio.sleep(delay)  # Asynchronously wait for the delay
    return (delay)
