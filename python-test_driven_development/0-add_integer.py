#!/usr/bin/python3
"""
This module defines a function that adds two integers.

"""
def add_integer(a, b=98):
    """
    add integer
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
