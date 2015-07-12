# recursive version of factorial

def factR(n):
    '''
    n is an int > 0
    return n!
    '''
    
    if n == 1:
        return n
    else:
        return n * factR(n - 1)