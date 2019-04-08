#segments in a plane

def gcd(a, b): #a < b
    if a == 0:
        return b
    return gcd(b % a, a)


def make_segment(startpoint, endpoint):
    return startpoint, endpoint


def start_point(segment):
    return segment[0]


def end_point(segment):
    return segment[1]


def make_point(x, y):
    return x, y


def xpoint(point):
    return point[0]


def ypoint(point):
    return point[1]


def midpoint_segment(segment):
    def average(a, b):
        return (a + b)/2

    p1 = start_point(segment)
    p2 = end_point(segment)

    return make_point(
        average(xpoint(p1), xpoint(p2)),
        average(ypoint(p1), ypoint(p2))
    )


s = make_segment(make_point(0, 1), make_point(2, 5))
print(midpoint_segment(s))
