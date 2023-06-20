
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Ex1: List Comprehension Scope in expression

print("With List Comprehension")
x = 10
lst = [x for x in range(5)]

print(f"{x=}")      # Output: 10
print(lst)          # Output: [0, 1, 2, 3, 4]


print("Without List Comprehension")

x = 10
lst = []

for x in range(5):
    lst.append(x)

print(f"{x=}")      # Output: 4
print(lst)          # Output: [0, 1, 2, 3, 4]

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Ex2: List Comprehension Scope in class scope

print("With List Comprehension")


class A:
    x = 10
    lst = [x for x in range(5)]

a = A()

print(f"{a.x=}")    # Output: 10
print(a.lst)        # Output: [0, 1, 2, 3, 4]


print("Without List Comprehension")

class B:
    x = 10
    lst = []

    for x in range(5):
        lst.append(x)

b = B()

print(f"{b.x=}")    # Output: 4
print(b.lst)        # Output: [0, 1, 2, 3, 4]


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# Ex3: List Comprehension Scope in class with global variables

print("With List Comprehension")

x = 5

class C:
    x = 10
    lst = [x for _ in range(5)]

c = C()

print(f"{c.x=}")    # Output: 10
print(c.lst)        # Output: [5, 5, 5, 5, 5]


print("Without List Comprehension")

x = 5

class D:
    x = 10
    lst = []

    for _ in range(5):
        lst.append(x)

d = D()

print(f"{d.x=}")    # Output: 10
print(d.lst)        # Output: [10, 10, 10, 10, 10]

# %%
