
def howMany(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    total = 0
    for i in aDict:
        total += len(aDict[i])
            
    return total