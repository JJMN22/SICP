changevalues = [1, 5, 10, 25]


def countchange(amount):
    def countways(amt, typesofchange):
        if typesofchange == 0 or amt < 0:
            return 0
        if amt == 0:
            return 1
        return countways(amt, typesofchange-1) + countways(amt-changevalues[typesofchange-1], typesofchange)
    print(countways(amount, len(changevalues)), "ways to count your change")


def printchange(amount):
    def getstrings(amt, typesofchange, string):
        if typesofchange == 0 or amt < 0:
            return ""
        if amt == 0:
            print(string)
            return ""
        newstr = string + str(changevalues[typesofchange-1]) + " "
        return getstrings(amt, typesofchange-1, string) + " " \
            + getstrings(amt-changevalues[typesofchange-1], typesofchange, newstr)
    getstrings(amount, len(changevalues), "")
    countchange(200)


print(countchange(100))
