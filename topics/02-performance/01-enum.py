from enum import Enum, auto


class Color(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()


class Role(Enum):
    ADMIN = "admin"
    OPERATOR = "operator"
    REPORTER = "reporter"


if __name__ == "__main__":
    print(f"{Color.RED=}")
    print(f"{Color.GREEN=}")
    print(f"{Color.BLUE=}")

    print()

    print(f"{Role.ADMIN=}")
    print(f"{Role.OPERATOR=}")
    print(f"{Role.REPORTER=}")

    assert Role["ADMIN"].name == "ADMIN"
    assert Role["ADMIN"].value == "admin"
