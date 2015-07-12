# check out if a character is in a string
# using bisection search recursively

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Base case: if aStr is empty, we did not find the char.
    if aStr == '':
        return False
    
    # Base case: if aStr is of length 1 or equals char
    elif char == aStr[(len(aStr) - 1) / 2]:
        return True
    
    # Recursive case
    elif char < aStr[(len(aStr) - 1) / 2]:
        return isIn(char, aStr[0:((len(aStr) - 1) / 2)])
    else:
        return isIn(char, aStr[(((len(aStr) - 1) / 2) + 1):])
    