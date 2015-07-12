# recursive version 2 of power

def recurPower2(base, exp):
    if exp == 0:
        return 1
    elif exp % 2 != 0:
        return base * recurPower2(base, exp - 1)
    else:
        return recurPower2(base * base, exp / 2)