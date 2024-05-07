#!/usr/bin/env python3
""" 2-measure_runtime.py module """
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Return the total time """
    start = start_time = time.time()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                         async_comprehension())
    return time.time() - start
