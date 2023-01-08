# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## Doing better with OOP


class FileHandler:
    def download(self, path):
        ...

    def upload(self, data, path):
        ...


class NewFileHandler:
    def download(self, path):
        ...

    def upload(self, data, path):
        ...


version = "new"
path_to_upload = "..."
path_to_download = "..."
data = b"..."

# create handler
if version == "old":
    handler = FileHandler()
elif version == "new":
    handler = NewFileHandler()  # type: ignore

# upload some data
handler.upload(data, path_to_upload)

# download some data
data = handler.download(path_to_download)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## Doing even better with Abstract Base Class


from abc import ABC, abstractmethod


class FileHandlerInterface(ABC):
    @abstractmethod
    def download(self, path):
        raise NotImplementedError

    @abstractmethod
    def upload(self, data, path):
        raise NotImplementedError


# create handler

class FileHandler2(FileHandlerInterface):
    def download(self, path):
        ...

    def upload(self, data, path):
        ...


# create new  handler

class NewFileHandler2(FileHandlerInterface):
    def download(self, path):
        ...

    def upload(self, data, path):
        ...


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Check an Example before continue

from typing import Protocol, runtime_checkable


@runtime_checkable
class Animal(Protocol):
    def walk(self) -> None:
        ...

    def speak(self) -> None:
        ...


class Dog:
    def walk(self) -> None:
        print("This is a dog walking")

    def speak(self):
        return "Woof!"


def make_animal_speak(animal: Animal):
    return animal.speak()


dog = Dog()
assert make_animal_speak(dog) == "Woof!"

# without @runtime_checkable this code will fail
assert isinstance(dog, Animal)

# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## Doing the bestest with Protocol and static analysis


from typing import Protocol


class Handler(Protocol):
    def download(self, path: str) -> bytes:
        ...

    def upload(self, data: bytes, path: str):
        ...


class FileHandler3:
    def download(self, path):
        ...

    def upload(self, data, path):
        ...


class NewFileHandler3:
    def download(self, path):
        ...

    def upload(self, data, path):
        ...


handler3: Handler  # this tells the static analyzer that handler is a Handler protocol, and any further assignments to it must match the Handler protocol

version = "new"
path_to_upload = "..."
path_to_download = "..."
data = b"..."

# create handler
if version == "old":
    handler3 = FileHandler3()
elif version == "new":
    handler3 = NewFileHandler3()


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
## Even better factories with metaprogramming

from typing import Dict, Protocol
from abc import abstractmethod


class Handler4(Protocol):
    def download(self, path: str) -> bytes:
        ...

    def upload(self, data: bytes, path: str) -> None:
        ...


class HandlerFactory:
    handlers: Dict = {}

    @classmethod
    def make_handler(cls, version) -> Handler4:
        try:
            retval = cls.handlers[version]()
        except KeyError as err:
            raise NotImplementedError(f"{version=} doesn't exist") from err
        return retval

    @classmethod
    def register(cls, type_name):
        def deco(deco_cls):
            cls.handlers[type_name] = deco_cls
            return deco_cls

        return deco


@HandlerFactory.register("old")
class FileHandler4:
    def download(self, path):
        ...

    def upload(self, data, path):
        ...


@HandlerFactory.register("new")
class NewFileHandler4:
    def download(self, path):
        ...

    def upload(self, data, path):
        ...


version = "new"
path_to_upload = "..."
path_to_download = "..."
data = b"..."

handler4 = HandlerFactory.make_handler(version)
handler4.upload(data, path_to_upload)
handler4.download(path_to_download)
print()

# %%
