def swapSort(L): 
    """ L is a list on integers """
    print "Original L: ", L
    for i in range(len(L)):
        #for j in range(len(L)):
        for j in range(i+1, len(L)):
            if L[j] < L[i]:
                # the next line is a short 
                # form for swap L[i] and L[j]
                L[j], L[i] = L[i], L[j] 
                print i,j,L
    print "Final L: ", L