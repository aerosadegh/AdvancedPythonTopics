

class Copyable(type):
    def __new__(cls, name, bases, dct):
        print("copyable new")
        obj = super().__new__(cls, name, bases, dct)

        def copy(self):
            return self.__class__(**self.__dict__)

        # def copy(self, deep=False):
        #     deep copy

        obj.copy = copy
        return obj


class Foo(metaclass=Copyable):
    def __init__(self, name, age, jobs=None) -> None:
        print("foo init")
        self.name = name
        self.age = age
        self.jobs = jobs or []


x = Foo("ali", 25, ["Python Programmer"])

y = x.copy()   # type: ignore

print(x.name, y.name)
print(x.age, y.age)
y.age += 1
print(x.age, y.age)
# y.jobs.append("student")
print(x.jobs, y.jobs)
