from timeit import timeit


code = "count_primes(100_000)"

# Part 1
print("Part 1")

t1 = timeit(
    code,
    setup="from count_primes import count_primes",
    number=1,
)
####################################
# Part 2
print("Part 2")

t2 = timeit(
    code,
    setup="from cypy_count_primes import count_primes",
    number=1,
)
####################################
# Part 3
print("Part 3")

t3 = timeit(
    code,
    setup="from cy_count_primes import count_primes",
    number=1,
)
####################################

# Report
print(f"Python: {t1:.3f} sec")
print(f"Cypython: {t2:.3f} sec")
print(f"Cython: {t3:.3f} sec")
print(f"Cypython is {t1/t2:.3f}x faster!")
print(f"Cython is {t1/t3:.3f}x faster!")

# Output:
# Python: 20.765 sec
# Cypython: 13.705 sec
# Cython: 0.896 sec
# Cypython is 1.515x faster!
# Cython is 23.167x faster!
