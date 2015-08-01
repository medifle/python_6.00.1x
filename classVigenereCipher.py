# from https://docs.google.com/forms/d/1gt4McfP2ZZkI99JFaHIFcP26lddyTREq4pvDnl4tl0w/viewform?c=0&w=1
# code written by bolo (github.com/medifle)

import string

class PHPGoAway(object):
    def __init__(self, key):
        self.key = key.lower().replace(" ", "")

    def setKey(self, key):
        '''key: a string.'''
        self.key = key.lower().replace(" ", "")
        
        
    def forLove(self, msg):
        '''msg: a string to be sent which only includes
        lowercase ascii characters and white space.
        Returns back the encrypted message.'''
        # convert to lowercase
        self.msg = msg.lower()
        
    def fromLove(self, msg):
        '''msg: message to be received
        Returns back the decrypted message.'''
        
    def genTable(self):
        '''Returns a table of 26 rows in the form of dict.
        Each alphabet shifted cyclically to the left compared to the previous alphabet,
        corresponding to the 26 possible Caesar ciphers.'''
        alphaTable = {}
        s = string.ascii_lowercase
        for i in range(26):
            alphaTable[s[0]] = s
            s = s[1:] + s[0]
        return alphaTable
        
    def genKeyWord(self):
        '''Returns keyword whose length matches the length of self.msg'''
        # compare lengths of two string and generate keyword accordingly
        if len(self.key) >= len(self.msg):
            self.keyWord = self.key[:len(self.msg)]
        else:
            self.keyWord = self.key * (len(self.msg) / len(self.key)) + self.key[:(len(self.msg) % len(self.key))]
        return self.keyWord