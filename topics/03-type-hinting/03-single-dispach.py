# %%%%

# Class: SingleDispatchMethod

from functools import singledispatchmethod


class Sum:

    @singledispatchmethod
    def sum_method(self, arg1, arg2):
        print(f"Default implementation with arg1 = {arg1} and arg2 = {arg2}")

    @sum_method.register
    def _(self, arg1: int, arg2: int):
        print(f"Sum with arg1 as integer. {arg1} + {arg2} = {arg1 + arg2}")

    @sum_method.register
    def _(self, arg1: float, arg2: float):
        print(f"Sum with arg1 as float. {arg1} + {arg2} = {arg1 + arg2}")

s = Sum()
s.sum_method(2, 3)
s.sum_method(2.1, 3.4)
s.sum_method("hi", 3.4)
s.sum_method(3+2j, 3.4)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Function: SingleDispatch

from functools import singledispatch

@singledispatch
def sum_method(arg1, arg2):
    print(f"Default implementation with arg1 = {arg1} and arg2 = {arg2}")

@sum_method.register
def _(arg1: int, arg2: int):
    print(f"Sum with arg1 as integer. {arg1} + {arg2} = {arg1 + arg2}")

@sum_method.register
def _(arg1: float, arg2: float):
    print(f"Sum with arg1 as float. {arg1} + {arg2} = {arg1 + arg2}")


sum_method(2, 3)
sum_method(2.1, 3.4)
sum_method("hi", 3.4)
sum_method(3+2j, 3.4)
# %%
