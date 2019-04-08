from lisplists import *


def r_reverselist(lisplist):  # recursively defined reverse
    if lisplist is None:
        return None
    first = car(lisplist)
    endlist = cdr(lisplist)
    return append(r_reverselist(endlist), cons(first, None))


def i_reverselist(sequence):  # iteratively defined reverse

    def i_helper(forward, reverse):
        if forward is None:
            return reverse
        return i_helper(cdr(forward), cons(car(forward), reverse))

    return i_helper(sequence, None)


def for_each(function, lisplist):

    def repeat(llist):
        function(car(llist))
        if cdr(llist) is not None:
            return repeat(cdr(llist))

    return repeat(lisplist)