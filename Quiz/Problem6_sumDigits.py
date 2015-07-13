def sumDigits(N):
    '''
    N: a non-negative integer
    Returns: a positive integer, the sum of N's digits
    '''
    if N / 10 == 0:
        return N
    return (N % 10) + sumDigits(N / 10)