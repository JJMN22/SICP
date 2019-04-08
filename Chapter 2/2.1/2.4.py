#car, cons, cdr as procedures
def cons(x, y):
    return lambda m: m(x, y)


def car(z):
    return z(lambda p, q: p)


def cdr(z):
    return z(lambda p, q: q)


def i():
    return cons(2, 12)


print(car(i()))
