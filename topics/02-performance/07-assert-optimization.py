"""
-O	Basic optimizations, such as removing dead code and inlining functions.
-OO	More aggressive optimizations, such as constant folding and loop optimization.
"""
import timeit
import math
from time import sleep
from random import choices
import statistics
from functools import total_ordering


@total_ordering
class Orders:
    def __init__(self, orders_annotation, orders_num):
        self.orders_annotation = orders_annotation
        self.orders_num = orders_num

    def __repr__(self):
        return self.orders_annotation

    def __eq__(self, __value: object) -> bool:
        return self.orders_num == __value

    def __lt__(self, __value: object) -> bool:
        return self.orders_num < __value


orders = [
    Orders("", 0),
    Orders("u", -3),
    Orders("m", -6),
    Orders("n", -9),
]


def slowest_condition(n):
    if choices([True, False], cum_weights=[0.001, 1]):
        sleep(0.01)
    return n


def factorial(n):
    """calculates the factorial of n

    Args:
        n (int)

    Returns:
        int: factorial of n
    """
    assert slowest_condition(n) >= 0, "n must be non-negative"
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def _order_of_magnitude(number):
    return math.floor(math.log(number, 10))


def convert_to_si_orders(number, decimal=2) -> str:
    omn = _order_of_magnitude(number)
    for idx, order in enumerate(orders, start=-1):
        if omn > order:
            break
    convert_number = number * 10 ** (-orders[idx].orders_num)
    return f"{convert_number:.{decimal}f} {orders[idx]}"


def main():
    for _ in range(10):
        factorial(10)


if __name__ == "__main__":
    t = timeit.repeat("main()", setup="from __main__ import main", number=3, repeat=5)
    var = statistics.stdev(t)
    mean = statistics.fmean(t)
    om = convert_to_si_orders(mean)
    ov = convert_to_si_orders(var)
    print(f"{om}s ± {ov}s")

    print(f"{__debug__ = }")
    print(f"factorial docstring:\n{factorial.__doc__}")


# NOTE: run this code in these three commands below
#   python     07-assert-optimization.py  # WARNING: it takes very long time
#   python -O  07-assert-optimization.py
#   python -OO 07-assert-optimization.py
