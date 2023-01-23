# My[py]

Mypy is a static type checker for Python.

Type checkers help ensure that you’re using variables and functions in your code correctly. With mypy, add type hints ([**PEP 484**](https://peps.python.org/pep-0484/)) to your Python programs, and mypy will warn you when you use those types incorrectly.

Python is a dynamic language, so usually you’ll only see errors in your code when you attempt to run it. Mypy is a _static_ checker, so it finds bugs in your programs without even running them!

Here is a small example to whet your appetite:

```python
number = input("What is your favourite number?")
print("It is", number + 1)  # error: Unsupported operand types for + ("str" and "int")
```

Adding type hints for mypy does not interfere with the way your program would otherwise run. Think of type hints as similar to comments! You can always use the Python interpreter to run your code, even if mypy reports errors.

Mypy is designed with gradual typing in mind. This means you can add type hints to your code base slowly and that you can always fall back to dynamic typing when static typing is not convenient.

Mypy has a powerful and easy-to-use type system, supporting features such as type inference, generics, callable types, tuple types, union types, structural subtyping and more. Using mypy will make your programs easier to understand, debug, and maintain.

## Built-in types

### Simple types

Here are examples of some common built-in types:

| Type | Description |
|---|---|
| `int` | integer |
| `float` | floating point number |
| `bool` | boolean value (subclass of `int`) |
| `str` | text, sequence of unicode codepoints |
| `bytes` | 8-bit string, sequence of byte values |
| `object` | an arbitrary object (`object` is the common base class) |

All built-in classes can be used as types.

### Any type

If you can’t find a good type for some value, you can always fall back to `Any`:

| Type | Description |
|---|---|
| `Any` | dynamically typed value with an arbitrary type |

The type `Any` is defined in the `typing` module.

### Generic types

In Python 3.9 and later, built-in collection type objects support indexing:

| Type | Description |
|---|---|
| `list[str]` | list of `str` objects |
| `tuple[int, int]` | tuple of two `int` objects (`tuple[()]` is the empty tuple) |
| `tuple[int, ...]` | tuple of an arbitrary number of `int` objects |
| `dict[str, int]` | dictionary from `str` keys to `int` values |
| `Iterable[int]` | iterable object containing ints |
| `Sequence[bool]` | sequence of booleans (read-only) |
| `Mapping[str, int]` | mapping from `str` keys to `int` values (read-only) |
| `type[C]` | type object of `C` (`C` is a class/type variable/union of types) |

The type `dict` is a _generic_ class, signified by type arguments within `[...]`. For example, `dict[int, str]` is a dictionary from integers to strings and `dict[Any, Any]` is a dictionary of dynamically typed (arbitrary) values and keys. `list` is another generic class.

`Iterable`, `Sequence`, and `Mapping` are generic types that correspond to Python protocols. For example, a `str` object or a `list[str]` object is valid when `Iterable[str]` or `Sequence[str]` is expected. You can import them from [`collections.abc`](https://docs.python.org/3/library/collections.abc.html#module-collections.abc "(in Python v3.11)") instead of importing from [`typing`](https://docs.python.org/3/library/typing.html#module-typing "(in Python v3.11)") in Python 3.9.

See [Using generic builtins](https://mypy.readthedocs.io/en/stable/runtime_troubles.html#generic-builtins) for more details, including how you can use these in annotations also in Python 3.7 and 3.8.

These legacy types defined in [`typing`](https://docs.python.org/3/library/typing.html#module-typing "(in Python v3.11)") are needed if you need to support Python 3.8 and earlier:

| Type | Description |
|---|---|
| `List[str]` | list of `str` objects |
| `Tuple[int, int]` | tuple of two `int` objects (`Tuple[()]` is the empty tuple) |
| `Tuple[int, ...]` | tuple of an arbitrary number of `int` objects |
| `Dict[str, int]` | dictionary from `str` keys to `int` values |
| `Iterable[int]` | iterable object containing ints |
| `Sequence[bool]` | sequence of booleans (read-only) |
| `Mapping[str, int]` | mapping from `str` keys to `int` values (read-only) |
| `Type[C]` | type object of `C` (`C` is a class/type variable/union of types) |

`List` is an alias for the built-in type `list` that supports indexing (and similarly for `dict`/`Dict` and `tuple`/`Tuple`).

Note that even though `Iterable`, `Sequence` and `Mapping` look similar to abstract base classes defined in [`collections.abc`](https://docs.python.org/3/library/collections.abc.html#module-collections.abc "(in Python v3.11)") (formerly `collections`), they are not identical, since the latter don’t support indexing prior to Python 3.9.
