from typing import Deque
from time import sleep
from collections import deque

d: Deque[int] = deque(maxlen=5)


for i in range(20):
    d.append(i)
    sleep(.5)
    print(d, end="\r", flush=True)


