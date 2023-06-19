from __future__ import annotations

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## Ex1: private method

# attr, __repr__, __str__, __hash__, __eq__


class Student:
    """class for describe students"""

    def __init__(self, name: str, age: int, student_number: int) -> None:
        self.name = name
        self.age = age
        self.student_number = student_number

    def __repr__(self):
        return f"{type(self).__name__}(name={self.name!r}, age={self.age!r}, student_number={self.student_number!r})"

    def __attrs(self):
        return (self.name, self.age, self.student_number)

    def __hash__(self) -> int:
        return hash(self.__attrs())

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__attrs() == other.__attrs()
        return NotImplemented


s1 = Student("Ali", 21, 202245)
s1

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Ex2: order and hash

# attr, __repr__, __str__, __hash__, __eq__, __ne__, __abs__, __gt__, __lt__


class Complex:
    def __init__(self, real: float, imag: float) -> None:
        self.real = real
        self.imag = imag

    def __repr__(self):
        return f"{type(self).__name__}(real={self.real!r}, imag={self.imag!r})"

    def __hash__(self) -> int:
        return hash((self.real, self.imag))

    def __eq__(self, other) -> bool:
        if isinstance(other, (int, float, complex, self.__class__)):
            return all([self.real == other.real, self.imag == other.imag])
        return NotImplemented

    ## __ne__ auto checked from __eq__ between Complex and Complex

    def __ne__(self, other) -> bool:
        if isinstance(other, (int, float, complex, self.__class__)):
            return all([self.real != other.real, self.imag != other.imag])
        return NotImplemented

    def __abs__(self) -> float:
        return pow(self.real**2 + self.imag**2, 0.5)

    def __gt__(self, other) -> bool:
        if isinstance(other, (int, float, complex, self.__class__)):
            return abs(self) > abs(other)
        return NotImplemented

    ## __lt__ auto checked from __gt__ between Complex and Complex

    def __lt__(self, other) -> bool:
        if isinstance(other, (int, float, complex, self.__class__)):
            return abs(self) < abs(other)
        return NotImplemented


c1 = Complex(3, 4)
print(c1)
c2 = Complex(-2, -7)
print(c2)
print("gt", c1 > c2)
print("lt", c1 < c2)
print("eq", c1 == c2)
print("ne", c1 != "abc")
print(hash(c1))
abs(c1)

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Ex3: repr!


class Person:
    """class for describe students"""

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{type(self).__name__}(name={self.name!r}, age={self.age!r})"  # child class
        # return f"{self.__class__.__name__}(name={self.name!r}, age={self.age!r})" # child class
        # return f"{__class__.__name__}(name={self.name!r}, age={self.age!r})"  # parent class


class Teacher(Person):
    def __init__(self, name: str, age: int, teacher_code) -> None:
        super().__init__(name, age)
        self.teacher_code = teacher_code


t1 = Teacher("Ali", 21, 202245)
t1

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Ex4: Scope


name = "Python"


class Rand:
    name = "RandClass"
    lst1 = [name] * 3
    lst2 = [name for i in range(3)]
    lst3 = [name] * 3
    lst4 = [name, name, name]

    def __repr__(self) -> str:
        return f"{type(self).__name__}(name={self.name!r})"


r = Rand()


# print(r.name)
print(r.lst1)
print(r.lst2)
print(r.lst3)
print(r.lst4)
r

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Ex5: Custom Dict: introducing the problem!

# from https://realpython.com/inherit-python-dict/


class UpperCase_dict1(dict):
    def __setitem__(self, key, value):
        key = key.upper()
        super().__setitem__(key, value)


d1 = UpperCase_dict1()
d1["one"] = 1  # correct
d1["two"] = 2  # correct
d1["three"] = 3  # correct

d1.update({"four": 4})  # incorrect
print(d1)


d2 = UpperCase_dict1({"one": 1, "two": 2, "three": 3})  # incorrect
d2 = UpperCase_dict1(one=1, two=2, three=3)  # incorrect
print(d2)


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Ex5: Fixed UpperCase_dict


class UpperCase_dict2(dict):
    def __init__(self, mapping=None, /, **kwargs):
        if mapping is not None:
            mapping = {str(key).upper(): value for key, value in mapping.items()}
        else:
            mapping = {}
        if kwargs:
            mapping.update({str(key).upper(): value for key, value in kwargs.items()})
        super().__init__(mapping)

    def __setitem__(self, key, value):
        key = key.upper()
        super().__setitem__(key, value)


d3 = UpperCase_dict2({"one": 1, "two": 2, "three": 3})  # correct
print(d3)


d3.update({"four": 4})  # incorrect
print(d3)


# Why do dict subclasses behave this way? Built-in types were designed and
# implemented with the `open–closed principle` in mind.
# Therefore, they’re open to extension but closed to modification.
# Allowing modifications to the core features of these classes can
# potentially break their `invariants`.
# So, Python core developers decided to protect them from modifications.


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Ex5: Fixed UpperCaseDict

from collections import UserDict


class UpperCaseDict(UserDict):
    def __setitem__(self, key, value):
        key = key.upper()
        super().__setitem__(key, value)


numbers = UpperCaseDict({"one": 1, "two": 2})
numbers["three"] = 3
numbers.update({"four": 4})
numbers.setdefault("five", 5)

numbers


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Ex6: Custom Dict :: Considering Performance

import timeit
from collections import UserDict


class ExtendedDict_dict(dict):
    def apply(self, action):
        for key, value in self.items():
            self[key] = action(value)

    def remove(self, key):
        del self[key]

    def is_empty(self):
        return len(self) == 0


class ExtendedDict_UserDict(UserDict):
    def apply(self, action):
        for key, value in self.items():
            self[key] = action(value)

    def remove(self, key):
        del self[key]

    def is_empty(self):
        return len(self) == 0


init_data = dict(zip(range(1000), range(1000)))

dict_initialization = min(
    timeit.repeat(
        stmt="ExtendedDict_dict(init_data)",
        number=1000,
        repeat=5,
        globals=globals(),
    )
)

user_dict_initialization = min(
    timeit.repeat(
        stmt="ExtendedDict_UserDict(init_data)",
        number=1000,
        repeat=5,
        globals=globals(),
    )
)

print(
    f"UserDict is {user_dict_initialization / dict_initialization:.3f}",
    "times slower than dict",
)



# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Ex7.1: Code with WRONG default value definition
from typing import List


class A:
    def __init__(self, items: List = []):  # wrong! list is mutable!
        self.items = items


a1 = A()
b1 = A()

a1.items.extend(["item1", "item2", "item3"])

print(f"{a1.items=}")
print(f"{b1.items=}")

# %%
# Ex7.2: Code with CORRECT default value definition
from typing import List, Optional


class B:
    def __init__(self, items: Optional[List] = None):
        self.items = items or list()  # correct! instantiate a list when construct object!


a2 = B()
b2 = B()

a2.items.extend(["item1", "item2", "item3"])

print(f"{a2.items=}")
print(f"{b2.items=}")

# %%
