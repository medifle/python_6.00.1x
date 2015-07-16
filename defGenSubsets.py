def genSubsets(L):
    '''
    L: list
    Returns: all subsets of L
    '''
    # base case
    if len(L) == 0:
        return [[]]
    # recursive block
    left = L[0:1]
    right = genSubsets(L[1:])
    combine = []
    for i in right:
        combine.append(left + i)
    return right + combine