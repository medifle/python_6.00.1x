# from https://docs.google.com/forms/d/1gt4McfP2ZZkI99JFaHIFcP26lddyTREq4pvDnl4tl0w/viewform?c=0&w=1
# code written by bolo (github.com/medifle)

import string

class PHPGoAway(object):
    def __init__(self, key):
        self.key = key.lower().replace(" ", "")

    def setKey(self, key):
        '''key: a string.'''
        self.key = key.lower().replace(" ", "")
        
        
    def forLove(self, plaintext):
        '''msg: a string to be sent which only includes
        lowercase ascii characters and white space.
        White space should be intact.
        Returns back the encrypted message.'''
        # each letter of plaintext determines which column to choose
        # each letter of keyword determines which row of alphabet table to choose
        # convert to lowercase
        plaintext = plaintext.lower()
        # initialize result and keyword
        result = ''
        keyword = self.genKeyWord(plaintext)
        # for each letter in keyword
        for i in range(len(keyword)):
            # if the letter of plaintext is a whitespace, keep the space intact
            if plaintext[i] == ' ':
                result += ' '
            # else, go along with the corresponding row of alphabet table and generate enciphered letter
            else:
                column = string.ascii_lowercase.index(plaintext[i])
                result += self.genTable()[keyword[i]][column]
        return result
        
    def fromLove(self, msgEncrypted):
        '''msgEncrypted: message to be received and decrypted
        Returns back the decrypted message.'''
        # initialize result and keyword
        result = ''
        keyword = self.genKeyWord(msgEncrypted)
        # for each letter in keyword
        for i in range(len(keyword)):
            # if the letter of msgEncrypted is a whitespace, keep the space intact
            if msgEncrypted[i] == ' ':
                result += ' '
            #else, go along with the corresponding row of alphabet table and generate plaintext letter
            else:
                column = self.genTable()[keyword[i]].index(msgEncrypted[i])
                result += string.ascii_lowercase[column]
        return result
            
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
        
    def genKeyWord(self, text):
        '''text could either be plaintext to be encrypted or encrypted message.
        Returns keyword whose length matches the length of text'''
	keyWord = ''
	count = 0
	for i in range(len(text)):
	    if text[i] == ' ':
		keyWord += ' '
		count += 1
   	    else:
       	        keyWord += self.key[(i - count) % len(self.key)]
        return keyWord