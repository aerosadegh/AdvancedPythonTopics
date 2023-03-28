# In Python, certain types are compatible even though they aren’t subclasses of each other.
# For example, int objects are valid whenever float objects are expected.
# Mypy supports this idiom via duck type compatibility.
# This is supported for a small set of built-in types:
"""
`int` is duck type compatible with `float` and `complex`.

`float` is duck type compatible with `complex`.
"""

# %%%%%%%%%%%%%%%%%%%%
import math

from decimal import Decimal
from fractions import Fraction

int_num = 2
float_num = 2.0
complex_num = 2.0 + 2j
decimal_num = Decimal("2.0")
fraction_num = Fraction(5, 6)
bool_val = True
str_val = "2.0"


def degrees_to_radians(degrees: float) -> float:
    return math.pi * degrees / 180


n = 90  # Inferred type 'int'
print(degrees_to_radians(n))  # Okay!
print(degrees_to_radians(float_num))  # Okay!
print(degrees_to_radians(bool_val))  # Okay!
# print(degrees_to_radians(fraction_num))  # NOT OK
# print(degrees_to_radians(decimal_num))  # NOT OK - raise Error


int_attrs = [item for item in dir(int_num) if not item.startswith("_")]
float_attrs = [item for item in dir(float_num) if not item.startswith("_")]
complex_attrs = [item for item in dir(complex_num) if not item.startswith("_")]
decimal_attrs = [item for item in dir(decimal_num) if not item.startswith("_")]
fraction_attrs = [item for item in dir(fraction_num) if not item.startswith("_")]
print(f"{int_attrs      = }")
print(f"{float_attrs    = }")
print(f"{complex_attrs  = }")
print(f"{decimal_attrs  = }")
print(f"{fraction_attrs = }")
print("\n  intersection:")
print(" ** int, float Type:")
print(set(int_attrs).intersection(float_attrs))
print("\n ** All numbers Type:")
print(set(int_attrs).intersection(float_attrs).intersection(complex_attrs).intersection(decimal_attrs).intersection(fraction_attrs))


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# General Number Type

from numbers import Number


assert isinstance(int_num, Number)
assert isinstance(float_num, Number)
assert isinstance(complex_num, Number)
assert isinstance(decimal_num, Number)
assert isinstance(fraction_num, Number)
assert isinstance(bool_val, Number)
# assert isinstance(str_val, Number)  # raise AssertionError
