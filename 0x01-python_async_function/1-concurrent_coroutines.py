#!/usr/bin/env python3
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random
"""
async takes integer
"""


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    return random for each
    """

    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = await asyncio.gather(*tasks)
    return sorted(delays)
