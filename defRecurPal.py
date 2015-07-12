# recursion on strings: check out palindrome

def recurPal(s):
    '''
    assumes s a string
    '''
    def toChars(s):
        s = s.lower()
        ans = ''
        for c in s:
            if c in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + c
        return ans
    
    def isPal(s):
        '''
        assumes s a string
        returns boolean value
        '''
        if len(s) == 0 or len(s) == 1:
            return True
        elif s[0] == s[-1]:
            return recurPal(s[1:-1])
        else:
            return False
    return (isPal(toChars(s)))


'''
def isPal(s):
    if len(s) <= 1:
        return True
    else:
        return s[0] == s[-1] and isPal(s[1:-1])
'''