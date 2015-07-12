
def num_digits(x):
    '''
    assumes num_digits(x) represents the number of digits in the integer x
    '''
    i = 1
    while x / (10 ** i) != 0:
        i += 1
    return i