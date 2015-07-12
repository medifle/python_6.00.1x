# recursive version of Towers of Hanoi

# fr means 'from'
# printMove print every step in order to complete the problem.
def printMove(fr, to):
    print('Move from ' + str(fr) + ' to ' + str(to))

# 'fr', 'to', 'spare' are the three towers
# 'fr' is the name of the tower you move stacks from
# 'to' is the name of the tower you want to move stacks to
# 'spare' is the third tower
# 'n' is the number of stacks
def Towers(n ,fr, to, spare):
    if n == 1:
        printMove(fr, to)
    else:
        Towers(n - 1, fr, spare, to)
        Towers(1, fr, to, spare)
        Towers(n - 1, spare, to, fr)