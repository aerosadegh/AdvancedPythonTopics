import time
from multiprocessing import Process, Event
from multiprocessing import synchronize

DELAY = 0.1


def get_duration(start, end) -> str:
    hours, rem = divmod(end - start, 3600)
    minutes, seconds = divmod(rem, 60)
    return f"{int(hours):0>2}:{int(minutes):0>2}:{seconds:05.2f}"


def monitor_func(t0, done: synchronize.Event, before="", after="") -> None:
    t1 = time.time()
    while True:
        msg = before + get_duration(t0, t1) + after
        status = f"\r {msg}"
        print(status, end="", flush=True)
        if done.wait(DELAY):
            break
        t1 = time.time()
    blanks = " " * len(status)
    print(f"\r{blanks}\r", end="")


def long_computation():
    # emulate a long computation
    time.sleep(3)
    return 42


if __name__ == "__main__":
    done = Event()
    spinner = Process(None, monitor_func, args=(time.time(), done, "Please wait ... "))
    spinner.start()
    res = long_computation()
    done.set()
    print()  # keep progress time
    spinner.join()
    print(f"Answer: {res}")
