#Interval Arithmetic:: Did not finish!!


def make_interval(a, b):
    return a, b


def lower_bound(z):
    return z[0]


def upper_bound(z):
    return z[1]


def sub_interval(i1, i2):
    low = lower_bound(i2) - upper_bound(i1) #lowest possible low point
    high = upper_bound(i2) - lower_bound(i1) #highest possible high point

    return make_interval(low, high)


def mul_interval(i1, i2): #represents 9 cases
    low1 = lower_bound(i1)
    high1 = upper_bound(i1)
    low2 = lower_bound(i2)
    high2 = upper_bound(i2)

    if low1 < 0 and high1 < 0:
        if low2 < 0 and high2 < 0:
            return make_interval(high1 * high2, low1 * low2)
        elif low2 < 0 < high2:
            return make_interval(low1 * high2, low1 * low2)
        elif low2 > 0 and high2 > 0:
            return make_interval(low1 * high2, high1 * low2)
    elif low1 < 0 < high1:
        if low2 < 0 and high2 < 0:
            return
        elif low2 < 0 < high2:
            return
        elif low2 > 0 and high2 > 0:
            return
    elif low1 > 0 and high1 > 0:
        if low2 < 0 and high2 < 0:
            return
        elif low2 < 0 < high2:
            return
        elif low2 > 0 and high2 > 0:
            return