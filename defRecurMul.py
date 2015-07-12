# recursive version of multiplication

def recurMul(a, b):
    if b < 0:
        a = -a
        b = -b
    if b == 0:
        return 0
    if b == 1:
        return a
    else:
        return a + recurMul(a, b - 1)
    