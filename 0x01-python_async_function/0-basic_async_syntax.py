#!/usr/bin/env python
"""
async waits for a random delay between 0 and max_delay
"""
# Importing Modules
import asyncio
import random
from typing import Union


async def wait_random(max_delay: int = 10) -> float:  # Defining the Coroutine
    """
    return a random delay
    """
    delay = random.uniform(0, max_delay)       # Generating a Random Delay
    await asyncio.sleep(delay)                 # Pausing the Coroutine
    return delay                               # Returning the Delay
