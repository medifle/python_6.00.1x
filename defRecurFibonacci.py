# recursive version of Fibonacci sequence

def recurFib(n):
    '''
    assumes x an int >= 0
    returns Fibonacci of x
    '''
    # if there is no assert statement here, 
    # typing any negative number will cause infinite recursion
    assert type(n) == int and n >= 0
    if n == 0 or n == 1:
        return 1
    else:
        return recurFib(n - 1) + recurFib(n - 2)