# apply a value to functions

def applyFuns(L, x):
    '''
    assumes L is a list of functions
    x is an int
    '''
    for f in L:
        print(f(x))