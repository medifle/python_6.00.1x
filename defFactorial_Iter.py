# iterative version of factorial

def factI(n):
    '''
    n is an int > 0
    return n!
    '''
    result = 1
    for a in range(n):
        result = result * n
        n -= 1
    return result