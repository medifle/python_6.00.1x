# Lec 3, Problem 9
# bisection search

print('Please think of a number between 0 and 100!')

low = 0
high = 100
x = '0'

while x != 'c':
    guess = (low + high) / 2
    
    print('Is your secret number ' + str(guess) + '?')
    x = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    
    if x == 'c':
        print('Game over. Your secret number was: ' + str(guess))
        break
    elif x == 'h':
        high = guess
    elif x == 'l':
        low = guess
    else:
        print('Sorry, I did not understand your input.')

