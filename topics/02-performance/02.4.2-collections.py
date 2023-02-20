from typing import NamedTuple


class Person(NamedTuple):
    """named tuple with default values"""

    name: str
    age: int
    height: float
    weight: float
    country: str = "Canada"


print(issubclass(Person, tuple))  # True

jane = Person("Jane", 25, 1.75, 67)
print(jane.name)  # 'Jane'
# Error
jane.name = "Jane Doe"  # type: ignore
