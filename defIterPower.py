# define x to the power of p

def iterativePower(x, p):
    result = 1

    for a in range(p):
        result = result * x
        
    return result

