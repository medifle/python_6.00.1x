# findRoot1

def findRoot(x, power, epsilon):
    '''
    x int or float
    power >= 1
    epsilon > 0
    '''
    
    if x < 0 and power % 2 == 0:
        return None
    # can't find even powered root of negative number
    
    low = min(-1, x)
    high = max(1, x)
    ans = (low + high) / 2.0
    
    # notice abs()
    while abs(ans ** power - x) > epsilon:
        if (ans ** power) < x:
            low = ans
        else:
            high = ans
        ans = (low + high) / 2.0
    return ans