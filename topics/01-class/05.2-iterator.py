# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Iterator example


class Iterator:
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


itr = Iterator(1, 2, 3, 4, 5)

try:
    print(f"Item index [3] is {itr[3]}\n")  # type: ignore
except Exception as e:
    print(e)
    print()

print("Part 1: Iterator Execution returns values")

for i in itr:
    print(i)

print("\nPart 2: Iterator Execution returns empty")

for i in itr:
    print(i)


# %%
