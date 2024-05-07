#!/usr/bin/env python3
""" 0-async_generator.py """
import asyncio
import random


async def async_generator():
    """ yild random from 0 - 1"""
    for _ in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(1)
