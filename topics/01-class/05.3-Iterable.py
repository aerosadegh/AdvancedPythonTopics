# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Iterable example


class ItemIterator:
    """Iterator class"""

    def __init__(self, *args) -> None:
        self.items = args
        self.__current_index = -1
        self.__items_len = len(self.items)

    def __iter__(self):
        return self

    def __next__(self):
        self.__current_index += 1
        if self.__current_index < self.__items_len:
            return self.items[self.__current_index]
        raise StopIteration


class Items:
    """Iterable class"""

    def __init__(self, *args) -> None:
        self.items = args

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return ItemIterator(*self.items)
        # return iter(self.items)


items = Items(1, 2, 3, 4, 5)

try:
    print(f"Item index [3] is {items[3]}\n")  # type: ignore
except Exception as e:
    print(e)
    print()

print("Part 1: Iterable Execution returns values")

for item in items:
    print(item)

print("\nPart 2: Iterable Execution returns values agian")

for item in items:
    print(item)

# %%
