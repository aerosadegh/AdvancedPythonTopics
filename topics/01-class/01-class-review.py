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
        if isinstance(other, (int, float, complex, Complex)):
            return all([self.real == other.real, self.imag == other.imag])
        return NotImplemented

    ## __ne__ auto checked from __eq__ between Complex and Complex

    def __ne__(self, other) -> bool:
        if isinstance(other, (int, float, complex, Complex)):
            return all([self.real != other.real, self.imag != other.imag])
        return NotImplemented

    def __abs__(self) -> float:
        return pow(self.real ** 2 + self.imag ** 2, 0.5)

    def __gt__(self, other) -> bool:
        if isinstance(other, (int, float, complex, Complex)):
            return abs(self) > abs(other)
        return NotImplemented

    ## __lt__ auto checked from __gt__ between Complex and Complex

    def __lt__(self, other) -> bool:
        if isinstance(other, (int, float, complex, Complex)):
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
        return f"{type(self).__name__}(name={self.name!r}, age={self.age!r})" # child class
        # return f"{self.__class__.__name__}(name={self.name!r}, age={self.age!r})" # child class
        # return f"{__class__.__name__}(name={self.name!r}, age={self.age!r})"  # parent class


class Teacher(Person):

    def __init__(self, name: str, age: int, teacher_code) -> None:
        super().__init__(name, age)
        self.teacher_code = teacher_code



t1 = Teacher("Ali", 21, 202245)
t1

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

