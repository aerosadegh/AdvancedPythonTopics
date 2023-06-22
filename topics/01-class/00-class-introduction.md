# Classes

from [python documentation](https://docs.python.org/3/tutorial/classes.html)

## 1. Definitions

Classes provide a means of bundling data and functionality together. Creating a new class creates a new type of object, allowing new instances of that type to be made. Each class instance can have attributes attached to it for maintaining its state. Class instances can also have methods (defined by its class) for modifying its state.

Compared with other programming languages, Python’s class mechanism adds classes with a minimum of new syntax and semantics. It is a mixture of the class mechanisms found in C++ and Modula-3.

**Python classes provide all the standard features of Object Oriented Programming:**

1. The class inheritance mechanism allows multiple base classes
2. A derived class can override any methods of its base class or classes
3. A method can call the method of a base class with the same name.

Objects can contain arbitrary amounts and kinds of data.
As is true for modules, classes partake of the dynamic nature of Python:

1. they are created at runtime
2. can be modified further after creation

```python
class ClassName:
    <statement-1>
    .
    .
    .
    <statement-N>
```

---

### 1.1 Simple Example

Ex1.

```python
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

>>> print(MyClass.__doc__)
"A simple example class"
>>> x = MyClass()
>>> x.f()
"hello world"
```

The instantiation operation (“calling” a class object) creates an empty object. Many classes like to create objects with instances customized to a specific initial state. Therefore a class may define a special method named `__init__()`

Ex2.

```python
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

>>> x = Complex(3.0, -4.5)
>>> x.r, x.i
(3.0, -4.5)
```

---

### 1.2 Class and Instance Variables

```python
class Dog:

    kind = 'canine'         # class variable shared by all instances

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.kind                  # shared by all dogs
'canine'
>>> e.kind                  # shared by all dogs
'canine'
>>> d.name                  # unique to d
'Fido'
>>> e.name                  # unique to e
'Buddy'
```

Shared data (a class variable) can have possibly surprising effects with involving mutable objects such as lists and dictionaries:

```python
class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks                # unexpectedly shared by all dogs
['roll over', 'play dead']
```

Correct design of the class should use an instance variable instead:

```python
class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)

>>> d = Dog('Fido')
>>> e = Dog('Buddy')
>>> d.add_trick('roll over')
>>> e.add_trick('play dead')
>>> d.tricks
['roll over']
>>> e.tricks
['play dead']
```

---

### 1.3 Inheritance

#### 1.3.1 Single Inheritance

```python
class DerivedClassName(BaseClassName):
    <statement-1>
    .
    .
    .
    <statement-N>
```

#### 1.3.2 Multiple Inheritance

```python
class DerivedClassName(Base1, Base2, Base3):
    <statement-1>
    .
    .
    .
    <statement-N>
```

---

### 1.4 Private Variables

There is a convention that is followed by most Python code:

* a name prefixed with an underscore (e.g. `_spam`) should be treated as a non-public part of the API (whether it is a function, a method or a data member).

It should be considered an implementation detail and subject to change without notice.

Since there is a valid use-case for class-private members (namely to avoid name clashes of names with names defined by subclasses), there is limited support for such a mechanism, called name mangling. Any identifier of the form `__spam` (at least two leading underscores, at most one trailing underscore) is textually replaced with `_classname__spam`, where classname is the current class name with leading underscore(s) stripped. This mangling is done without regard to the syntactic position of the identifier, as long as it occurs within the definition of a class.

```python
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   # private copy of original update() method

class MappingSubclass(Mapping):

    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)
```

The above example would work even if `MappingSubclass` were to introduce a `__update` identifier since it is replaced with `_Mapping__update` in the Mapping class and `_MappingSubclass__update` in the `MappingSubclass` class respectively. [code](00-class-introduction.py)

#### 1.4.1 Private vs Protected Methods

from [[here](https://jellis18.github.io/post/2022-01-15-access-modifiers-python/)]

Private means that the attribute/method can only be used inside the class where it is defined. Protected means that the attribute/method can only be used in the class where it is defined or its subclasses.

Ok, so how do we use this? What does it actually do? And why would we do it? Lets look at a convoluted, but illuminating example:

```python
class Thing:
    def __init__(self, public: str, *, protected: str = "protected", private: str = "private"):
        self.public = public
        self._protected = protected
        self.__private = private

    def info(self) -> None:
        print(
            (
                f"This class has public attribute: {self.public}, "
                f"protected attribute: {self._protected}, "
                f"and private attribute: {self.__private}"
            )
        )
```

and then

```python
>>> thing = Thing("public")

# this is fine because it is assessing the variables internally in the info method
>>> thing.info()
'This class has public attribute: public, protected attribute: protected, and private attribute: private'

# this is also fine because the public attribute is indeed public
>>> print(thing.public)
'public'

# this will run but will give an error when checked with pylance
>>> print(thing._protected)
'"_protected" is protected and used outside of the class in which it is declared'

# this will not actually run and will raise an AttributeError but it will also give an error when checked
>>> print(thing.__private)
'"__private" is private and used outside of the class in which it is declared'
```

Let's inherit from this class

```python
class SomeThing(Thing):
    def more_info(self) -> None:
        print(f"This class has public attribute: {self.public}, protected attribute: {self._protected}")

    def use_private(self) -> None:
        print(f"Private attribute is {self.__private}")

>>> some_thing = SomeThing("public")

# still can use the info method which uses the private attribute internally
>>> some_thing.info()
'This class has public attribute: public, protected attribute: protected, and private attribute: private'

# can use the new more_info method that uses the public and protected attribute
>>> some_thing.more_info()
'This class has public attribute: public, protected attribute: protected'

# this will raise an AttributeError and will also give an error when checked
>>> some_thing.use_private()
'"__private" is private and used outside of the class in which it is declared'
```

##### When Use

protected and private variables are part of a concept known as **information hiding** which deals with hiding implementation details from downstream users.

1. private attributes/methods should be used in cases where you don't want downstream users or developers to have access to that attribute or method. This is good for hiding implementation details which may be prone to change but will not affect downstream users.

2. protected attributes/methods should be used where developers can have access (through subclassing) but not outside users. This is useful for defining methods to be implemented by subclasses (through ABCs) which are then used in the parent class through a code re-use mechanism.

If you use protected attributes/methods and allow for subclassing then these attributes/methods essentially become part of the public API since other developers can have access to them in their subclasses. This means that a change to the protected implementation in the parent class will affect all subclasses.

[See Also This Code](03-abstract.py) and [This Tutorial](03.1-protocol.md)

Ex

```python
from abc import ABC, abstractmethod
from typing import List, TypeVar

import numpy as np

T = TypeVar("T", bound="Model")


class Model(ABC):
    def __init__(self):
        self._is_fitted = False

    def fit(self: T, data: np.ndarray, target: np.ndarray) -> T:
        fitted_model = self._fit(data, target)
        self._is_fitted = True
        return fitted_model

    def predict(self, data: np.ndarray) -> List[float]:
        if not self._is_fitted:
            raise ValueError(f"{self.__class__.__name__} must be fit before calling predict")
        return self._predict(data)

    @property
    def is_fitted(self) -> bool:
        return self._is_fitted

    @abstractmethod
    def _fit(self: T, data: np.ndarray, target: np.ndarray) -> T:
        pass

    @abstractmethod
    def _predict(self, data: np.ndarray) -> List[float]:
        pass
```
