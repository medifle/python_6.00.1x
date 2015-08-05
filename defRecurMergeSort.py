def merge(L):
    '''L: a list
    Returns: a sorted list'''
    # base case
    if len(L) == 1:
        return L
    # splits list L in half
    L1 = L[0:len(L)/2]
    L2 = L[len(L)/2:]
    L1S = merge(L1)
    L2S = merge(L2)
    
    # merge two sorted list
    new = []
    while len(new) != len(L):
        if len(L1S) == 0:
            new.extend(L2S)
        elif len(L2S) == 0:
            new.extend(L1S)
        elif L1S[0] > L2S[0]:
            new.append(L2S[0])
            del L2S[0]
        else:
            new.append(L1S[0])
            del L1S[0]
    return new