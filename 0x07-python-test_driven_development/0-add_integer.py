#!/usr/bin/python3
"""
A module with a function to add two numbers(integers or floats)

"""
def add_integers(a, b=98):
    """
    Function to add two numbers(int or float)

    Args:
        a: first number
        b: second number

        a and b must be casted to int first

    Raises:
        TypeError: If a or b are not integers or floats

    Return:
        The addition of the two numbers

    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError('a must be an integer')
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError('b must be an integer')
    a = int(a)
    b = int(b)
    return (a + b)
