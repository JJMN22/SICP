def cons(a, b):
    if type(b) is not tuple:  # check if b is same type as lisplists
        return makelist(a, b)
    else:
        return a, b


def car(z):
    return z[0]


def cdr(z):
    return z[1]


def cadr(z):
    return car(cdr(z))


def caddr(z):
    return cadr(cdr(z))


def ispair(z):
    return type(z) is tuple and len(z) == 2


def makelist(*args):

    temp = list(args)

    def make(array):
        if len(array) == 0:
            return None
        return array.pop(0), make(array)
    return make(temp)


def printl(lisplist):
    def print_helper(li):
        if li is None:
            return
        elif type(car(li)) is tuple:  # nested case
            print("(", end="")
            print_helper(car(li))
            if cdr(li) is None:
                print(")", end="")
            else:
                print(")", end=" ")
        else:
            if cdr(li) is None:
                print(car(li), end="")
            else:
                print(car(li), end=" ")

        print_helper(cdr(li))  # recursive step

    print_helper(lisplist)
    print("\n", end="")  # newline at the end


def lastvalue(lisplist):
    if lisplist is None:
        raise Exception("Cannot find last value of null list")
    elif cdr(lisplist) is None:
        return car(lisplist)
    return lastvalue(cdr(lisplist))


def append(lisplist1, lisplist2):
    if lisplist1 is None:
        return lisplist2
    return cons(car(lisplist1), append(cdr(lisplist1), lisplist2))


def length(lisplist):
    if lisplist is None:
        return 0
    return 1 + length(cdr(lisplist))


def mapl(procedure, sequence):
    if sequence is None:
        return None
    return cons(procedure(car(sequence)), mapl(procedure, cdr(sequence)))


def accumulatel(op, initial, lisplist):
    if lisplist is None:
        return initial
    return op(car(lisplist), accumulatel(op, initial, cdr(lisplist)))


def filterl(predicate, lisplist):
    if lisplist is None:
        return None
    if predicate(car(lisplist)):
        return cons(predicate, filterl(predicate, cdr(lisplist)))
    return filterl(predicate, cdr(lisplist))


def flatmap(op, lisplist):
    return accumulatel(append, None, mapl(op, lisplist))


