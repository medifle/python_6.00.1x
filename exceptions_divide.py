count = 0
def divide(x, y):
    global count
    
    try:
        result = x / y
    except ZeroDivisionError, e:
        print 'division by zero!', e
    except TypeError, e:
        divide(int(x), int(y))
    else:
        print 'result is', result
        print count
    finally:
        count += 1
        print "executing 'finally' clause", count
        print type(x)