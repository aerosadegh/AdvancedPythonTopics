from typing import DefaultDict, List
from collections import defaultdict
from random import choice, randint
from string import ascii_lowercase

db: DefaultDict[int, List] = defaultdict(list)


def password_generator(length):
    return "".join([choice(ascii_lowercase) for _ in range(length)])


password_list = [password_generator(randint(8, 12)) for _ in range(20)]

for password in password_list:
    db[len(password)].append(password)

for password_length, passwords in db.items():
    print(password_length, passwords)
