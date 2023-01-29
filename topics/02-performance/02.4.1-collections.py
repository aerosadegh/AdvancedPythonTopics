from collections import namedtuple


Person = namedtuple(
    "Person",
    [
        "name",
        "age",
        "height",
        "weight",
    ],
)


print(issubclass(Person, tuple)) # True

jane = Person("Jane", 25, 1.75, 67)
print(jane.name)  # 'Jane'

jane.name = "Jane Doe"  # Error