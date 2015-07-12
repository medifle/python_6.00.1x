# exponential function

def iterPower(a, b):
    result = a
    if b == 0:
        result = 1
    while b - 1 > 0:
        result *= a
        b -= 1
    return result