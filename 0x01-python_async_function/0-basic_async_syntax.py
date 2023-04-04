#!/usr/bin/env python3
"""
This module contains the  wait_random
"""

import asyncio
import random


async def wait_random(max_delay: int=10) -> float:
    """
    returns random delay between 0 and max_delay
    args:
        max_delay (int): maximum length of wait time
    return:
        delay_time (float): the actual delay time
    """

    delay_time: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay_time)
    return delay_time
