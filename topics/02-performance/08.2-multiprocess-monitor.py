import sys
import time
import multiprocessing

DELAY = 0.1


def get_duration(start, end) -> str:
    hours, rem = divmod(end - start, 3600)
    minutes, seconds = divmod(rem, 60)
    return f"{int(hours):0>2}:{int(minutes):0>2}:{seconds:05.2f}"


def monitor_func(t0, welcome_message):
    write, flush = sys.stdout.write, sys.stdout.flush
    t1 = time.time()
    write(f"{welcome_message}\n")
    while True:
        msg = get_duration(t0, t1)
        write(msg)
        flush()
        write("\x08" * len(msg))
        time.sleep(DELAY)
        t1 = time.time()


def long_computation():
    # emulate a long computation
    time.sleep(3)


if __name__ == "__main__":
    spinner = multiprocessing.Process(
        None, monitor_func, args=(time.time(), "Start Monitoring\nPlease wait ... ")
    )
    spinner.start()
    try:
        long_computation()
        print("\nComputation done")
    finally:
        spinner.terminate()
