# iterative version of length of a string

def lenIter(aStr):
    '''
    aStr: a string
    returns: int, the length of aStr
    '''
    count = 0
    for a in aStr:
        count += 1
    return count