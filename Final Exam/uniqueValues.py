def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''
    if len(aDict) == 0:
        return []
    Lst = []
    for k1 in aDict:
        uniqFlag = True
        b = aDict.copy()
        del b[k1]
        for k2 in b:
            if b[k2] == aDict[k1]:
                uniqFlag = False
                break
        if uniqFlag:
            Lst.append(k1)
    return sorted(Lst)