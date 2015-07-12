# iterative version of greatest common divisor

def gcdIter(a, b):
    gcd = min(a, b)
    while gcd > 0:
        if a % gcd == 0 and b % gcd == 0:
            return gcd
        gcd -= 1
    