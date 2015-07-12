# you can assume lo < hi

def clip(lo, x, hi):
    '''
    '''
    a = max(lo, x)
    b = min(a, hi)
    return b