# sharp function

def sharp(x):
    '''
    x is in int >= 2
    '''
    assert x >= 2
    
    if x == 2:
        return 2
    else:
        return sharp(x - 1) ** x   