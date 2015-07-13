# remove duplicates in two lists

def removeDups0(L1, L2):
    # this block of code doesn't work as expected
    for a in L1:
        if a in L2:
            L1.remove(a)

def removeDups1(L1, L2):
    l = len(L1)
    while l > 0:
        if L1[0] in L2:
            L1.remove(L1[0])
        l -= 1

def removeDups2(L1, L2):
    # note that using L1Clone = L1 is the same as removeDups0
    # L1[:] makes a copy
    L1Clone = L1[:]
    for a in L1Clone:
        if a in L2:
            L1.remove(a)