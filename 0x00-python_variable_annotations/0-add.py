#!/usr/bin/env python3
"""
python3 -c 'print(__import__("my_module").__doc__)'
python3 -c 'print(__import__("my_module").MyClass.__doc__)'
python3 -c 'print(__import__("my_module").my_function.__doc__)'
python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'
"""

"""
This module provides basic annotations add
"""


def add(a: float, b: float) -> float:

    """
    Return the sum of a and b.

    Parameters:
    a (float): The first number.
    b (float): The second number.
    Returns:
    float: The sum of a and b.
    """

    return a + b
