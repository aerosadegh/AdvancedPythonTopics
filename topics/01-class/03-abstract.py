""" Abstract Base Class (abc) in Python """

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# abstractmethod


from abc import ABC, abstractmethod


class Polygon(ABC):
    @abstractmethod
    def noofsides(self):
        pass


class Triangle(Polygon):

    # overriding abstract method
    def noofsides(self):
        return 3


class Pentagon(Polygon):

    # overriding abstract method
    def noofsides(self):
        return 5


# Driver code
R = Triangle()
assert R.noofsides() == 3


P = Pentagon()
assert P.noofsides() == 5

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# application


def side(p: Polygon):
    return p.noofsides()


print(side(R))

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

from abc import ABC, abstractmethod, abstractproperty


class parent(ABC):
    @abstractproperty
    def run(self):
        return "parent class"


class child(parent):
    @property
    def run(self):
        return "child class"


try:
    r = parent()  # type: ignore
    print(r.run)
except Exception as err:
    print(err)

r = child()
print(r.run)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# register() : Register subclass as a “virtual subclass” of this ABC.

from abc import ABC


class MyABC(ABC):
    pass


MyABC.register(tuple)

assert issubclass(tuple, MyABC)
assert isinstance((1,), MyABC)
print()


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


from abc import ABC, abstractmethod


class Calculation(ABC):
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def subtract(self):
        pass


@Calculation.register
class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    # def subtract(self):
    #     return self.a - self.b


take = Calculator(10, 5)
assert take.add() == 15
# subtract method is an abstract method but it is not throwing error due to virtual sub class
# take.subtract()
assert Calculator.mro() == [Calculator, object]  # True
assert issubclass(Calculator, Calculation)  # True -> Virtual

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# alternative method to abc

from abc import ABCMeta, abstractmethod


class Calculation2(metaclass=ABCMeta):
    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def subtract(self):
        pass

    def multiply(self):
        pass

    def division(self):
        pass


class Calculator2(Calculation2):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def subtract(self):
        return self.a - self.b


assert Calculator2.mro() == [Calculator2, Calculation2, object]  # True

take2 = Calculator2(10, 5)
assert take2.add() == 15
assert take2.subtract() == 5


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

from abc import ABCMeta, abstractmethod


class Shape:

    __metaclass__ = ABCMeta

    def __init__(self, shapeType):
        self.shapeType = shapeType

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, breadth):
        Shape.__init__(self, Rectangle)
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def perimeter(self):
        return 2 * (self.length + self.breadth)


class Circle(Shape):
    pi = 3.14

    def __init__(self, radius):
        Shape.__init__(self, Circle)
        self.radius = radius

    def area(self):
        return round(Circle.pi * (self.radius ** 2), 2)

    def perimeter(self):
        return round(2 * Circle.pi * self.radius, 2)


rectangle = Rectangle(30, 15)
assert rectangle.area() == 450
assert rectangle.perimeter() == 90
