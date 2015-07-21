import matplotlib.pyplot as plt
import string


def loadWords():
    '''Returns a list containing the words from PSET 4'''

    fin = open('/Users/bolo/githubRepo/python_6.00.1x/HashGraphs/words.txt', 'r')
    wordList = []
    for line in fin:
        wordList.append(line.strip().lower())
    return wordList
    fin.close()
    
##--------------------------------------------------------    
## The following three hash functions were given to us.

def firstHashFunction(s):
    return string.ascii_lowercase.index(s[0])

def secondHashFunction(s):
    return string.ascii_lowercase.index(s[-1])

def thirdHashFunction(s):
    total = 0
    for char in s:
        total += string.ascii_lowercase.index(char)
    return total % 26
##----------------------------------------------------------

def doHashing(hashFunction):
    '''Takes as argument one of the three hash functions defined.
    Returns a dictionary containing a frequency distribution of all integers
    returned by the hash function.'''
    
    wordList = loadWords()
    hashedDict = {}
    for w in wordList:
        #Convert each word in the wordList to its corresponding hash.
        hashedWord = hashFunction(w)
        
        #Create a frequency distribution of all the integers returned by the hash function.
        hashedDict[hashedWord] = hashedDict.get(hashedWord, 0) + 1
    return hashedDict

def plotHash(hashFunction):
    ''' Takes as argument one of the hash functions defined. Plots frequency distribution
    of all the integers returned by the hash function.'''
    
    plt.bar(doHashing(hashFunction).keys(),doHashing(hashFunction).values(),facecolor='#9999ff', edgecolor='white')
    plt.ylabel('Number of words in wordlist')
    plt.xlabel('Hash')
    plt.title(hashFunction)
    plt.axis([0, 26, 0, 10000])
    plt.show()
