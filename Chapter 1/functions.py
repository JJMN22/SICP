# 1.41, 1.42, 1.43


def fixedpoint(function, firstguess):
    tolerance = 0.001

    def close_enough(num1, num2):
        return abs(num1 - num2) < tolerance

    def tryguess(guess):
        nextguess = function(guess)
        if close_enough(guess, nextguess):
            return guess
        return tryguess(nextguess)

    return tryguess(firstguess)


def repeated(function, repetitions):
    def compose(f, g):
        return lambda a: f(g(a))

    if repetitions == 1:
        return lambda x: function(x)
    return compose(function, repeated(function, repetitions-1))


def averagedamp(function):
    return lambda a: (a + function(a))/2


def double(function):
    return lambda a: function(function(a))


def square(num):
    return pow(num, 2)


def inc(num):
    return num + 1


print(repeated(square, 2)(5))
