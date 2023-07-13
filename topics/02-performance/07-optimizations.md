# Run in Optimization mode

Python provides two command-line options for optimizing code: `-O` and `-OO`.

```bash
python -O code.py
python -OO code.py
```

When you run Python with the -O option, the bytecode optimizer removes assert statements, but it does not clear the `__doc__` strings from the compiled bytecode. The `__doc__` strings are still present in the compiled bytecode and accessible at runtime. This can result in smaller bytecode files and slightly faster execution times.

On the other hand, when you run Python with the `-OO` option, the bytecode optimizer not only removes assert statements and `__doc__` strings, but also removes all assert-related code, such as the `__debug__` variable and the assert keyword itself. This can result in even smaller bytecode files and slightly faster execution times, but at the cost of losing the ability to use assert statements for debugging.

It's worth noting that the performance gains from using these options are usually small, and may not be noticeable in most cases. Additionally, removing assert statements and `__doc__` strings can make debugging and understanding code more difficult, so it's generally recommended to only use these options when you're sure they won't cause any issues.

## Constant Folding

In Constant Folding, the engine finds and evaluates constant expressions at compile time rather than computing them at runtime, making the runtime leaner and faster.

```python
>>> day_sec = 24 * 60 * 60
```

When the compiler encounters a constant expression, like above, it evaluates the expression and replaces it with the evaluated value. The expression is usually replaced by the evaluated value in the Abstract Syntax Tree, but the implementation is totally up to the language. Hence the above expression is effectively executed as

```python
>>> day_sec = 86400
```

Constant Folding in Python
In Python, we could use the Disassembler module to get the CPython bytecode giving us a good peek at how things will be executed. When we disassemble the above constant expression using the dis module, we get the following bytecode

```python
>>> import dis
>>> dis.dis("day_sec = 24 * 60 * 60")

        0 LOAD_CONST               0 (86400)
        2 STORE_NAME               0 (day_sec)
        4 LOAD_CONST               1 (None)
        6 RETURN_VALUE
```
