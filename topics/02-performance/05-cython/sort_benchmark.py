from timeit import timeit
from random import randint, seed


def get_values():
    return [randint(1, 10000) for _ in range(700)]


code = "sort(get_values())"


# Part 1
seed(200)

t1 = timeit(
    code,
    setup="from sort import sort",
    number=1000,
    globals={"get_values": get_values},
)
####################################
# Part 2
seed(200)

t2 = timeit(
    code,
    setup="from csort import sort",
    number=1000,
    globals={"get_values": get_values},
)
####################################

# Report
print(f"Python: {t1:.3f} sec")
print(f"Cython: {t2:.3f} sec")
print(f"Cython is {t1/t2:.3f}x faster!")

# Output:
# Python: 34.444 sec
# Cython: 0.668 sec
# Cython is 51.535x faster!
