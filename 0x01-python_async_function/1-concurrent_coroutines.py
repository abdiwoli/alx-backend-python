#!/usr/bin/env python3
""" 1-concurrent_coroutines.py """
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ wait n times calling random_wait """
    arr = []
    for i in range(n):
        arr.append(wait_random(max_delay))
    res = await asyncio.gather(*arr)
    return sorted(res)
