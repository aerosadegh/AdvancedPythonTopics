from random import choice
from string import ascii_lowercase
from collections import Counter


lst = [choice(ascii_lowercase) for _ in range(50)]

counter = Counter(lst)

sum_count = 0

for idx, (char, count) in enumerate(counter.most_common()):
    print(f"{idx+1:02}) {char = } repeated for {count} times!")
    sum_count += count

print(f"{sum_count = }")
