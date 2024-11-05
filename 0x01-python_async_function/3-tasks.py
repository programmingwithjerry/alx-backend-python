#!/usr/bin/env python3
"""
Function that returns an asyncio.Task for the `wait_random` coroutine.
"""

import asyncio
from typing import Any


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Creates and returns an asyncio.Task for the
       `wait_random` coroutine with the given max_delay."""
    return asyncio.create_task(wait_random(max_delay))
