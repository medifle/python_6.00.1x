def satisfiesF(L):
    """
    Assumes L is a list of strings
    Assume function f is already defined for you and it maps a string to a Boolean
    Mutates L such that it contains all of the strings, s, originally in L such
            that f(s) returns True, and no other elements
    Returns the length of L after mutation
    """
    Lclone = L[:]
    for i in Lclone:
        if not f(i):
            L.remove(i)
    return len(L)

#-----used for submitting-----
# run_satisfiesF(L, satisfiesF)


#-----test case-----
# def f(s):
#     return 'a' in s
#       
# L = ['a', 'b', 'bc', 'c', 'ab']
# print satisfiesF(L)
# print L