
# Importing Modules
import asyncio
import random
"""
async waits for a random delay between 0 and max_delay
"""


async def wait_random(max_delay: int = 10) -> float:  # Defining the Coroutine
    delay = random.uniform(0, max_delay)       # Generating a Random Delay
    await asyncio.sleep(delay)                 # Pausing the Coroutine
    return delay                               # Returning the Delay
