from __future__ import annotations

## Ex1

# attr, __repr__, __str__, __hash__

class Student:
    """class for describe students"""

    def __init__(self, name: str, age: int, student_number: int) -> None:
        self.name = name
        self.age = age
        self.student_number = student_number

    def __repr__(self):
        return f"{__class__.__name__}(name={self.name}, age={self.age}, student_number={self.student_number})"

    def __hash__(self) -> int:
        return hash((self.name, self.age, self.student_number))


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# Ex2

# attr, __repr__, __str__, __hash__, __eq__, __ne__, __abs__, __gt__, __lt__


class Complex:
    def __init__(self, real: float, imag: float) -> None:
        self.real = real
        self.imag = imag

    def __repr__(self):
        return f"{__class__.__name__}(real={self.real}, imag={self.imag})"

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


#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
print()