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


seq = Seq(1, 2, 3, 4, 5)


print(f"Item index: {seq[3]}\n")

for idx in range(len(seq)):  # type OK
    print(seq[idx])

print()

for item in seq:  # type Error! => "Seq" has no attribute "__iter__" (not iterable)mypy
    print(item)

# %%
