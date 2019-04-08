from lisplists import *
from math import *


def real_part(z):
    car(z)


def imag_part(z):
    cdr(z)


def mag(z):
    car(z)


def angle(z):
    cdr(z)


def make_from_real_imag(x, y):
    return cons(x, y)


def make_from_mag_ang(r, a):
    return cons(r * cos(a), r * sin(a))


def add_complex(z1, z2):
    return make_from_real_imag(
        real_part(z1) + real_part(z2),
        imag_part(z1) + imag_part(z2)
    )


def sub_complex(z1, z2):
    return make_from_real_imag(
        real_part(z1) - real_part(z2),
        imag_part(z1) - imag_part(z2)
    )


def mul_complex(z1, z2):
    return make_from_mag_ang(
        mag(z1) * mag(z2),
        angle(z1) + angle(z2)
    )


def div_complex(z1, z2):
    return make_from_mag_ang(
        mag(z1) / mag(z2),
        angle(z1) - angle(z2)
    )
