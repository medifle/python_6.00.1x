def genFib():
    c = 10
    fibn_1 = 1 #fib(n - 1)
    fibn_2 = 0 #fib(n - 2)
    while c > 0:
        # fib(n) = fib(n - 1) + fib(n - 2)
        next = fibn_1 + fibn_2
        yield next
        fibn_2 = fibn_1
        fibn_1 = next
        c -= 1

# --Sample Test START--
# a = genFib() # create an instance of genFib
# a.next() # yield first next and halt
# a.next() # yield second next and halt
# a.next() # yield third next and halt

# genFib().next() # create an instance of genFib and yield first next and halt
# genFib().next() # create other instance of genFib and yield first next and halt
# genFib().next() # create another instance of genFib and yield first next and halt

# for s in genFib(): print s #create an instance of genFib and print all the yields within the instance
# --Sample Test START--