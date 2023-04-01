from timeit import timeit

code = "factorial(1000)"


t1 = timeit(
    code,
    setup="from fact import factorial",
    number=1000
)

t2 = timeit(
    code,
    setup="from cfact import factorial",
    number=1000
)

print(f"Python: {t1:.3f} sec")
print(f"Cython: {t2:.3f} sec")
print(f"Cython is {t1/t2:.3f}x faster!")

# Output:
# Python: 0.283 sec
# Cython: 0.001 sec
# Cython is 303.587x faster!
