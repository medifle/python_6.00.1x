from ps4a import *
import time

def constructWord(hand, word):
    """
    check if the given hand could construct the given word
    hand: dictionary
    word: string
    returns string
    """
    check = None
    wordDic = getFrequencyDict(word)
    for i in wordDic:
        if (wordDic[i] > hand.get(i, None)) or (i not in hand):
            check = 0
    if check == 0:
        return ''
    else:
        return word


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    # Create a new variable to store the maximum score seen so far (initially 0)
    maxScore = 0
    # Create a new variable to store the best word seen so far (initially None)  
    bestWord = None
    # For each word in the wordList
    for i in wordList:
        # If you can construct the word from your hand
        # (hint: you can use isValidWord, or - since you don't really need to test if the word is in the wordList - you can make a similar function that omits that test)
        wordCons = constructWord(hand, i)
        if len(wordCons) > 0:
            # Find out how much making that word is worth
            wordScore = getWordScore(wordCons, n)
            # If the score for that word is higher than your best score
            if wordScore > maxScore:
                # Update your best score, and best word accordingly
                maxScore = wordScore
                bestWord = wordCons
    # return the best word you found.
    return bestWord


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # initialize total score
    totalScore = 0
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:
        # Display the hand
        print 'Current Hand: ',
        displayHand(hand)
    
        # Ask computer for input
        compInput = compChooseWord(hand, wordList, n)
        
        # If the word can be constructed:
        try:
            if len(compInput) > 0:
                # Show how many points the word earned, and the updated total score
                totalScore += getWordScore(compInput, n)
                print ('"' + compInput +'"' + ' earned ' +str(getWordScore(compInput, n))+ ' points. Total: ' + str(totalScore) + ' points')
                print
                # Update the hand 
                hand = updateHand(hand, compInput)
        # If the word cannot be constructed:
        except TypeError:
            break

    # Game is over, show total score
    print ('Total score: ' + str(totalScore) + ' points.')
    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    lastHand = {}
    n = HAND_SIZE
    
    #as long as you do not input e:
    while True:
        # Ask user for input
        userInput = raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        
        if userInput == 'n':
            lastHand = dealHand(n)
            while True:
                userInput2 = raw_input('Enter u to have yourself play, c to have the computer play: ')
                if userInput2 == 'u':
                    playHand(lastHand, wordList, n)
                    break
                elif userInput2 == 'c':
                    compPlayHand(lastHand, wordList, n)
                    break
                else:
                    print('Invalid command.')
            
        elif userInput == 'r':
            # check whether you have played at least one hand
            if len(lastHand) > 0:
                while True:
                    userInput2 = raw_input('Enter u to have yourself play, c to have the computer play: ')
                    if userInput2 == 'u':
                        playHand(lastHand, wordList, n)
                        break
                    elif userInput2 == 'c':
                        compPlayHand(lastHand, wordList, n)
                        break
                    else:
                        print('Invalid command.')
            else:
                print('You have not played a hand yet. Please play a new hand first!')
        elif userInput == 'e':
            break
        else:
            print('Invalid command.')

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


