#!/usr/bin/env python3
""" docimentation of the file """
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ task wiat documentation """
    """Returns an asyncio Task that waits for a random delay."""
    return asyncio.create_task(wait_random(max_delay))
