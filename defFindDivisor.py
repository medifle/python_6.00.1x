# find all common divisors

def findDivisors(n1, n2):
    """assumes that n1 and n2 are positive ints
    returns a tuple containing the common divisors of n1 and n2"""
    # the empty tuple
    divisors = ()
    
    for i in range(1, min(n1, n2) + 1):
        if n1 % i == 0 and n2 % i == 0:
            
            # in this case, '+' is an overloaded plus operator
            divisors = divisors + (i,)
    
    return divisors