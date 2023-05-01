"""
The Python standard shell, or REPL (Read-Eval-Print Loop), allows you to run Python code interactively while working on a project or learning the language.
"""

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# interning integers in the range [-5, 256]
print("$$$$$$$$  Integer Interning or Integer Caching  $$$$$$$$\n")
i = 256
j = 256

print(f"{i=} {j=} -> {(i is j) = }")
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# not interning integers out of range [-5, 256]

m = 257
n = 257
print(f"{m=} {n=} -> {(m is n) = }")


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# NOTE:
print(
    """
The integer caching feature is useful and necessary to reduce time and memory costs.
There are three facts under the hood:

1. The integers in the range of [-5, 256] are singletons in Python and can’t be recreated again.
2. If the Python compiler can see the whole code, more optimisations may apply to the code.
3. Different implementations and versions of Python may have different mechanisms for the same feature.
"""
)
print("#" * 50)
print()

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# interning strings
print("$$$$$$$$  String Interning  $$$$$$$$\n")

a = "python"
b = "python"
print(f"{a=} {b=} -> {(a is b) = }")


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# not interning strings (space)
c = "Python Programming"
d = "Python Programming"
print(f"{c=} {d=} -> {(c is d) = }")


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# interning (length) python 3.8+
e = "Y" * 4096
f = "Y" * 4096
print(f"'Y' * 4096 -> {(e is f) = }")

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# not interning (length)
g = "Y" * 4097
h = "Y" * 4097
print(f"'Y' * 4097 -> {(g is h) = }")

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# intern mannually

import sys

u = sys.intern("Y" * 4097)
v = sys.intern("Y" * 4097)
print(f"interned 'Y' * 4097 -> {(u is v) = }")

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# NOTE:
print(
    """
Why string interning is important?
Let’s assume that you have an application where a lot of string operations are happening.
If we were to use equality operator == for comparing long strings Python tries to compare it character by character and obviously it will take some time.
But if these long strings can be interned then we know that they point to the same memory location.
In such a case we can use is keyword for comparing memory locations as it works much faster.
"""
)

# %%
"""Now Run Code in Python Interpreter!"""
