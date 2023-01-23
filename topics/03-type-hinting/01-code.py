# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## Variables

# This is how you declare the type of a variable
age: int = 1

# You don't need to initialize a variable to annotate it
a: int  # Ok (no value at runtime until assigned)

# Doing so is useful in conditional branches
child: bool
if age < 18:
    child = True
else:
    child = False


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## Useful built-in types

# For most types, just use the name of the type
num_int: int = 1
num_flt: float = 1.0
var_bol: bool = True
var_str: str = "test"
var_byt: bytes = b"test"

# # For collections on Python 3.9+, the type of the collection item is in brackets
# x: list[int] = [1]
# x: set[int] = {6, 7}

# # For mappings, we need the types of both keys and values
# x: dict[str, float] = {"field": 2.0}  # Python 3.9+

# # For tuples of fixed size, we specify the types of all the elements
# x: tuple[int, str, float] = (3, "yes", 7.5)  # Python 3.9+

# # For tuples of variable size, we use one type and ellipsis
# x: tuple[int, ...] = (1, 2, 3)  # Python 3.9+


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# On Python 3.8 and earlier, the name of the collection type is
# capitalized, and the type is imported from the 'typing' module
from typing import List, Set, Dict, Tuple

x: List[int] = [1]
s: Set[int] = {6, 7}
d: Dict[str, float] = {"field": 2.0}
t: Tuple[int, str, float] = (3, "yes", 7.5)
w: Tuple[int, ...] = (1, 2, 3)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
### Structural types
from typing import Union, Optional, List

# # On Python 3.10+, use the | operator when something could be one of a few types
# q: list[int | str] = [3, 5, "test", "fun"]  # Python 3.10+
# # On earlier versions, use Union
q: List[Union[int, str]] = [3, 5, "test", "fun"]

# Use Optional[X] for a value that could be None
# Optional[X] is the same as X | None or Union[X, None]
r: Optional[str] = "something" if True else None
# Mypy understands a value can't be None in an if-statement
if r is not None:
    print(r.upper())
# If a value can never be None due to some invariants, use an assert
assert r is not None
print(r.upper())


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## Functions

from typing import Callable, Iterator, Union, Optional, List

# This is how you annotate a function definition
def stringify(num: int) -> str:
    return str(num)


# And here's how you specify multiple arguments
def plus(num1: int, num2: int) -> int:
    return num1 + num2


# If a function does not return a value, use None as the return type
# Default value for an argument goes after the type annotation
def show(value: str, excitement: int = 10) -> None:
    print(value + "!" * excitement)


# This is how you annotate a callable (function) value
ff: Callable[[int, float], float] = lambda x, y: y

# A generator function that yields ints is secretly just a function that
# returns an iterator of ints, so that's how we annotate it
def g(n: int) -> Iterator[int]:
    i = 0
    while i < n:
        yield i
        i += 1


# You can of course split a function annotation over multiple lines
def send_email(
    address: Union[str, List[str]],
    sender: str,
    cc: Optional[List[str]],
    bcc: Optional[List[str]],
    subject: str = "",
    body: Optional[List[str]] = None,
) -> bool:
    ...


# Mypy understands positional-only and keyword-only arguments
# Positional-only arguments can also be marked by using a name starting with
# two underscores
def quux(x: int, y: int) -> None:
    pass


quux(3, y=5)  # Ok
quux(x=3, y=5)  # error: Unexpected keyword argument "x" for "quux"

# This says each positional arg and each keyword arg is a "str"
def call(self, *args: str, **kwargs: str) -> str:
    def make_request(*args, **kwargs):
        ...
    reveal_type(args)  # Revealed type is "tuple[str, ...]"
    reveal_type(kwargs)  # Revealed type is "dict[str, str]"
    request = make_request(*args, **kwargs)
    return self.do_api_query(request)



# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## Classes

from typing import ClassVar, List


class MyClass:
    # You can optionally declare instance variables in the class body
    attr: int
    # This is an instance variable with a default value
    charge_percent: int = 100

    # The "__init__" method doesn't return anything, so it gets return
    # type "None" just like any other method that doesn't return anything
    def __init__(self) -> None:
        ...

    # For instance methods, omit type for "self"
    def my_method(self, num: int, str1: str) -> str:
        return num * str1

# User-defined classes are valid as types in annotations
my_class: MyClass = MyClass()

# You can also declare the type of an attribute in "__init__"
class Box:
    def __init__(self) -> None:
        self.items: List[str] = []

# You can use the ClassVar annotation to declare a class variable
class Car:
    seats: ClassVar[int] = 4
    passengers: ClassVar[List[str]]

# If you want dynamic attributes on your class, have it
# override "__setattr__" or "__getattr__":
# - "__getattr__" allows for dynamic access to names
# - "__setattr__" allows for dynamic assignment to names
class A:
    # This will allow assignment to any A.x, if x is the same type as "value"
    # (use "value: Any" to allow arbitrary types)
    def __setattr__(self, name: str, value: int) -> None: ...

    # This will allow access to any A.x, if x is compatible with the return type
    def __getattr__(self, name: str) -> int: ...

aa = A()

aa.foo = 42  # Works
aa.bar = 'Ex-parrot'  # Fails type checking  


# %%
