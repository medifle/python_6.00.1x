def iterativeFib(n):
    '''
    assumes x an int >= 0
    returns Fibonacci of x
    '''
    assert type(n) == int and n >= 0
    a = 1
    b = 1
    count = 1
    result = 1
    while count < n:
        result = a + b
        c = result
        a = b
        b = c
        count += 1
    return result