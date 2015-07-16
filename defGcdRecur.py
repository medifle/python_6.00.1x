# recursive version of greatest common divisor
# Euclidean algorithm

def gcdRecur(a, b):
    # base case
    if b == 0:
        return a
    # recursive block
    else:
        t = a
        a = b
        b = t % b
        return gcdRecur(a, b)