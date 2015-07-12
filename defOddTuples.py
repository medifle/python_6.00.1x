# odd tuples

def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    ans = ()
    i = 0
    l = len(aTup)
    while l > 0:
        ans += (aTup[i],) # equivalent of ans += aTup[i:i + 1]
        l -= 2
        i += 2
    return ans
    