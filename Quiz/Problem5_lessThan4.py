def lessThan4(aList):
    '''
    aList: a list of strings
    Returns: a list of strings which contain fewer than 4 characters
    '''
    ansList = []
    for i in aList:
        if len(i) < 4:
            ansList.append(i)
    return ansList