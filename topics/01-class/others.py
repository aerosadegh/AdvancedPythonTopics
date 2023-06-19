
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# List Comprehension Scope

print("With List Comprehension")
x = 10
lst = [x for x in range(5)]

print(f"{x=}")   # Output: 10
print(lst) # Output: [0, 1, 2, 3, 4]


print("Without List Comprehension")

x = 10
lst = []

for x in range(5):
    lst.append(x)

print(f"{x=}")    # Output: 4
print(lst) # Output: [0, 1, 2, 3, 4]

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

