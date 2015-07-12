# radiationExposure

def f(x):
    '''
    n is a float
    '''
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''
    rectNum = int((stop - start) / step)
    
    x = []
    for ix in range(rectNum):
        x = x + [start + ix * step]
    
    y = []
    for iy in x:
        y = y + [f(iy)]
    
    total = []
    for it in y:
        total = total + [it * step]
    
    return sum(total)