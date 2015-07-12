
def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    bigger = -1
    key = None
    for i in aDict:
        if len(aDict[i]) > bigger:
            bigger = len(aDict[i])
            key = i
    return key