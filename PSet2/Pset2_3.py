# using bisection search to make the program faster

balance = 999999
annualInterestRate = 0.18

a = balance
lowerBound = balance / 12
upperBound = (balance * (1 + annualInterestRate / 12) ** 12) / 12.0
minimumPaid = (lowerBound + upperBound) / 2.0
while abs(balance - 0) > 0.01:
    balance = a
    for month in range(1, 13):
        unpaidBalance = balance - minimumPaid
        interest = annualInterestRate / 12.0 * unpaidBalance
        balance = unpaidBalance + interest
    if balance > 0:
        lowerBound = minimumPaid
    else:
        upperBound = minimumPaid
    minimumPaid = (lowerBound + upperBound) / 2.0
print ('Lowest Payment: ' + str(round(minimumPaid, 2)))