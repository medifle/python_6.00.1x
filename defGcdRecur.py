# recursive version of greatest common divisor
# Euclidean algorithm

def gcdRecur(a, b):
    if b == 0:
        return a
    else:
        t = a
        a = b
        b = t % b
        return gcdRecur(a, b)