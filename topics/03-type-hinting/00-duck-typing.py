# In Python, certain types are compatible even though they aren’t subclasses of each other. 
# For example, int objects are valid whenever float objects are expected. 
# Mypy supports this idiom via duck type compatibility. 
# This is supported for a small set of built-in types:
"""
`int` is duck type compatible with `float` and `complex`.

`float` is duck type compatible with `complex`.
"""


import math


def degrees_to_radians(degrees: float) -> float:
    return math.pi * degrees / 180


n = 90  # Inferred type 'int'
print(degrees_to_radians(n))  # Okay!


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
int_methods = [item for item in dir(2) if not item.startswith("_")]
float_methods = [item for item in dir(2.2) if not item.startswith("_")]
print(f"{int_methods =     }")
print(f"{float_methods =   }")
print("\n  intersection:")
print(set(int_methods).intersection(float_methods))
