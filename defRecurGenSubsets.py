def genSubsets(L):
    '''
    L: list
    Returns: all subsets of L
    '''
    # base case
    if len(L) == 0:
        return [[]]
    # recursive block
    # all the subsets of smaller  + all the subsets of smaller combined with extra = all subsets of L
    extra = L[0:1]
    smaller = genSubsets(L[1:])
    combine = []
    for i in smaller:
        combine.append(extra + i)
    return smaller + combine