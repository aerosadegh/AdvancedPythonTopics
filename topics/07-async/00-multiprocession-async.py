import multiprocessing
import concurrent.futures

import time
from random import shuffle


def perform_task(task):
    time.sleep(task)  # Simulate a long-running task
    return f"Task {task} completed"


if __name__ == "__main__":
    tasks = list(range(3, 10))
    shuffle(tasks)
    print(tasks)
    with multiprocessing.Pool() as pool:
        results = [pool.apply_async(perform_task, (task,)) for task in tasks]
        while results:
            for i, result in enumerate(results):
                if result.ready():
                    print(result.get())
                    del results[i]
                    break

    # more pythonic way
    print("\n$$$ more pythonic way $$$\n")
    with concurrent.futures.ProcessPoolExecutor() as executor:
        futures = [executor.submit(perform_task, task) for task in tasks]
        for future in concurrent.futures.as_completed(futures):
            print(future.result())
