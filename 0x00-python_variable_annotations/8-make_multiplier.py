#!/usr/bin/env python3
""" 8-make_multiplier.py """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ return callable function """
    def multiplier_function(x: float) -> float:
        return multiplier * x
    return multiplier_function
