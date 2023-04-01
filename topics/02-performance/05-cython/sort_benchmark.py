from timeit import timeit
from random import randint

values = [randint(1, 1000) for _ in range(1000)]
code = "sort(values)"


t1 = timeit(
    code,
    setup="from sort import sort",
    number=1000,
    globals={"values": values},
)

t2 = timeit(
    code,
    setup="from csort import sort",
    number=1000,
    globals={"values": values},
)

print(f"Python: {t1:.3f} sec")
print(f"Cython: {t2:.3f} sec")
print(f"Cython is {t1/t2:.3f}x faster!")

# Output:
# Python: 34.444 sec
# Cython: 0.668 sec
# Cython is 51.535x faster!