"""
Singleton Example
"""
from typing import Dict


class SimpleSingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances : Dict = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Onei(metaclass=SimpleSingletonMeta):
    def __init__(self, age=0.05) -> None:
        self.age = age


if __name__ == "__main__":
    onei = Onei(10)
    print(onei.age)

    onei2 = Onei(20)
    print(onei2.age)
