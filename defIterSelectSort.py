# selection sort algorithm
# complexity is O(len(L)^2)

def iterSelectSort(L):
    for i in range(len(L) - 1):
        minIndex = i
        minVal = L[i]
        j = i + 1
        while j < len(L):
            if L[j] < minVal:
                minVal = L[j]
                minIndex = j
            j += 1
        temp = L[i]
        L[i] = L[minIndex]
        L[minIndex] = temp
    return L