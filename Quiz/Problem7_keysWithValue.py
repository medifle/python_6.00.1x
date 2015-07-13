def keysWithValue(aDict, target):
    '''
    aDict: a dictionary in which keys and values are both integers
    target: an integer
    Returns a list of keys in aDict with the value target
    '''
    ans = []
    for i in aDict:
        if aDict[i] == target:
            ans.append(i)
    return ans