# python


def factorial(n):
    f = 1
    for i in range(n):
        f *= n - i
    return f
