# apply each value of a function to the element of a list

def applyToEach(L, f):
    '''
    assumes L is a list
    f is a function
    '''
    for i in range(len(L)):
        L[i] = f(L[i])