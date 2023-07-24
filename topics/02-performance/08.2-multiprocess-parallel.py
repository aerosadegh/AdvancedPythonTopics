import multiprocessing
from time import perf_counter


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
        print(f"({self.label}) time took:\t{self.took:.5f} (sec)")


def long_running_calculation(x):
    # Simulate a long-running calculation
    result = 0
    for i in range(10000000):
        result += i * x
    return result


if __name__ == "__main__":
    # Perform the calculation without using multiprocessing
    with Timeit("without multiprocessing"):
        results = [long_running_calculation(x) for x in range(10)]
    # Perform the calculation using multiprocessing
    with Timeit("with multiprocessing"):
        with multiprocessing.Pool() as pool:
            results = pool.map(long_running_calculation, range(10))
