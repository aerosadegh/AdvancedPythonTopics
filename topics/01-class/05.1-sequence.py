# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Sequence example


class Seq:
    """Minimal Sequence Example"""

    def __init__(self, *args):
        self.items = args

    def __len__(self):
        return len(self.items)

    def __getitem__(self, key):
        return self.items[key]

    def __iter__(self):
        return iter(self.items)


seq = Seq(1, 2, 3, 4, 5)


print(f"Item index [3] is {seq[3]}\n")

print("Part 1: Sequence Execution returns values")

for idx in range(len(seq)):  # type OK
    print(seq[idx])

print("\nPart 2: Sequence Execution returns values again")

# if has not __iter__ get type Error!
# MyPy => "Seq" has no attribute "__iter__" (not iterable)mypy
for item in seq:
    print(item)

# %%
