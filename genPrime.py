def genPrimes():
    p = []
    x = 1
    while True:
        check = 1
        x += 1
        for i in p:
            if x % i == 0:
                check = 0
                break
        if check == 1:
            p.append(x)
            yield x
    
# --Sample Test START--
a = genPrimes()
print a.next()
print a.next()
print a.next()
print a.next()
# --Sample Test START--

# --Alternative START--
# Note that our solution makes use of the for/else clause, which 
# you can read more about here:
# http://docs.python.org/release/1.5/tut/node23.html 

# def genPrimes():
#     primes = []   # primes generated so far
#     last = 1      # last number tried
#     while True:
#         last += 1
#         for p in primes:
#             if last % p == 0:
#                 break
#         else:
#             primes.append(last)
#             yield last

# --Alternative END--