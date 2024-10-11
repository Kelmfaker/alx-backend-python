#!/usr/bin/env python3

"""
function takes a string and an int or float
"""


from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    return a tuple
    """
    x = float(v * v)
    return (k, x)
