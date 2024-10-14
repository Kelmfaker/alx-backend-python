#!/usr/bin/env python3
import asyncio
import random
wait_random = __import__('0-basic_async_syntax').wait_random
"""
async takes integer 
"""


async def wait_n(n: int, max_delay: int) -> float:
    """
    return 
