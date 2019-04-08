#use accumulate() to define basic lisplist manipulations

from lisplists import *


def map_accumulate(p, sequence): #maps a function onto each item in the list
    return accumulatel(
        lambda x, y: cons(p(x), y),
        None,
        sequence
    )


def append_accumulate(seq1, seq2): #appends list2 to list1
    return accumulatel(cons, seq2, seq1)


def length_accumulate(sequence): #finds the length of the list
    return accumulatel(lambda x, y: y+1, 0, sequence)


def identity(x):
    return x


z = makelist(1, 2, 3, 4, 5, 6, 7)


