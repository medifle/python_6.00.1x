# metered version of Fibonacci

def fibMetered(n):
    '''
    assumes x an int >= 0
    returns Fibonacci of x
    '''
    global numCalls
    numCalls += 1    
    assert type(n) == int and n >= 0
    if n == 0 or n == 1:
        return 1
    else:
        return fibMetered(n - 1) + fibMetered(n - 2)
        
def testFib(n):
    for i in range(n + 1):
        global numCalls
        numCalls = 0
        print('fib of ' + str(i) + ' = ' + str(fibMetered(i)))
        print('fib called ' + str(numCalls) + ' times')