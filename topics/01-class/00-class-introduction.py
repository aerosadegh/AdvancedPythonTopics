# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# private methods


class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        print("Calling `update` in `Mapping` class")
        for item in iterable:
            self.items_list.append(item)

    __update = update  # private copy of original update() method


class MappingSubclass(Mapping):
    def update(self, keys, values):
        # provides new signature for update()
        # but does not break __init__()
        print("Calling `update` in `MappingSubclass` class")
        for item in zip(keys, values):
            self.items_list.append(item)

    __update = update


# %%
ms = MappingSubclass([1, 2, 3])

# %%
ms._Mapping__update([7, 8, 9])  # type: ignore
ms.items_list


# %%
ms._MappingSubclass__update([1, 2, 3], [7, 8, 9])  # type: ignore
ms.items_list

# %%


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#  Private vs Protected methods


class Thing:
    def __init__(
        self, public: str, *, protected: str = "protected", private: str = "private"
    ):
        self.public = public
        self._protected = protected
        self.__private = private

    def info(self) -> None:
        print(
            (
                f"This class has public attribute: {self.public}, "
                f"protected attribute: {self._protected}, "
                f"and private attribute: {self.__private}"
            )
        )


# %%

thing = Thing("public")

# this is fine because it is assessing the variables internally in the info method
thing.info()

# this is also fine because the public attribute is indeed public
print(thing.public)

# this will run but will give an error when checked with pylance
print(thing._protected)

# %%%
# this will not actually run and will raise an AttributeError but it will also give an error when checked
print(thing.__private)
'"__private" is private and used outside of the class in which it is declared'


# %%

# Inheritance

class SomeThing(Thing):
    def more_info(self) -> None:
        print(
            f"This class has public attribute: {self.public}, protected attribute: {self._protected}"
        )

    def use_private(self) -> None:
        print(f"Private attribute is {self.__private}")


# %%%
some_thing = SomeThing("public")

# still can use the info method which uses the private attribute internally
some_thing.info()

# can use the new more_info method that uses the public and protected attribute
some_thing.more_info()

# %%

# this will raise an AttributeError and will also give an error when checked
some_thing.use_private()
