from time import perf_counter


def memoize(function):
    memo = {}

    def wrapper(*args, **kwargs):
        kw = tuple(sorted(kwargs.items()))
        cache_key = (args, kw)
        if cache_key in memo:
            return memo[cache_key]
        else:
            rv = function(*args, **kwargs)
            memo[cache_key] = rv
            return rv

    return wrapper


class Timeit:
    def __init__(self, label):
        self.label = label
        self.took = None
        self.t0 = None

    def __enter__(self):
        self.t0 = perf_counter()
        return self

    def __exit__(self, exc_type, exc_value, trace):
        t1 = perf_counter()
        self.took = t1 - self.t0
        print(f"({self.label}) time took: {self.took:.5f} (sec)")


# without cache
def fib(n):
    if n in [0, 1]:
        return n
    return fib(n - 2) + fib(n - 1)


# with cache
@memoize
def fib_cached(n):
    if n in [0, 1]:
        return n
    return fib_cached(n - 2) + fib_cached(n - 1)


if __name__ == "__main__":
    import sys

    sys.setrecursionlimit(1000)
    n = 30
    with Timeit("W/O Cache") as timer:
        res = fib(n)
    with Timeit("W Cache") as timer_cached:
        res_cached = fib_cached(n)

    print(f"Result with cache is {timer.took/timer_cached.took:.0f}X faster!")

    print(f"{'res':>12} = {res:<12}")
    print(f"{'res_cached':>12} = {res_cached:<12}")
