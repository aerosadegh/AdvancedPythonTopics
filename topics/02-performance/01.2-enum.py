from typing import Tuple
from enum import Enum


class MyEnum(Enum):
    @classmethod
    def names(cls):
        return list(cls.__members__.keys())

    @classmethod
    def values(cls):
        return list(cls.__members__.values())


class TubineType(MyEnum):

    MGT40: Tuple[str, str] = ("MGT-40", "")
    MGE40: Tuple[str, str] = ("MGT-40", "GE-Frame6")
    V942V3: Tuple[str, str] = ("V94.2", "V3")
    MGT70: Tuple[str, str] = ("MGT-70", "map2b")

    def __init__(self, ttname, ttversion):  # `name` property reserved for enum
        self.ttname = ttname
        self.ttversion = ttversion


if __name__ == "__main__":

    assert TubineType["MGT40"] == TubineType.MGT40
    assert TubineType["MGT40"].name == "MGT40"
    assert TubineType["MGT40"].value == ("MGT-40", "")

    assert TubineType["MGT70"].ttname == TubineType.MGT70.ttname
    assert TubineType["MGT70"].ttversion == TubineType.MGT70.ttversion

    assert TubineType.names() == ["MGT40", "MGE40", "V942V3", "MGT70"]
    assert TubineType.values() == [
        TubineType.MGT40,
        TubineType.MGE40,
        TubineType.V942V3,
        TubineType.MGT70,
    ]
