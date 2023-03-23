
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# point.py - property

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        try:
            self._x = float(value)
            print(f"Validated! x: {value}")
        except ValueError:
            raise ValueError('"x" must be a number') from None

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        try:
            self._y = float(value)
            print(f"Validated! y: {value}")
        except ValueError:
            raise ValueError('"y" must be a number') from None
        
print("1: ")
Point(1, 2)
print("2: ")
Point("5", "7")
print("3: ")
p2 = Point("2", "a")

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# point.py - descriptor

class Coordinate:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        try:
            instance.__dict__[self._name] = float(value)
            print(f"Validated! {self._name}: {value}")
        except ValueError:
            raise ValueError(f'"{self._name}" must be a number') from None

class Point:
    x = Coordinate()
    y = Coordinate()

    def __init__(self, x, y):
        self.x = x
        self.y = y

print("1: ")
Point(1, 2)
print("2: ")
Point("5", "7")
print("3: ")
p2 = Point("2", "a")
# %%
