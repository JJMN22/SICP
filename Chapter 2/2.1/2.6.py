#Church numerals
def zero():
    return lambda f: lambda x: x


def add1(n):
    return lambda f: lambda x: f(n(f), x)


def one():
    return lambda f: lambda x: f(x)


def two():
    return lambda f: lambda x: f(f(x))


def church_add(a, b):
    return lambda f: lambda x: a(f(b(f(x))))


print(one())
print(two())