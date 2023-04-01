# cython: language_level=3


cpdef int factorial(int n):
    cdef int f = 1
    cdef int i

    for i in range(n):
        f *= (n - i)
    return f