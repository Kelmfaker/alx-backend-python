#!/usr/bin/env python3

"""
function takes a float multuplier
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    return a function that multiplies a float by multiplier
    """
    def multiplies(x: float) -> float:
        """
        return the result
        """
        return x * multiplier
    return multiplies
