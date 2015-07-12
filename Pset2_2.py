# paying debt off in a year

balance = 3329
a = balance
annualInterestRate = 0.2
minimumPaid = 10

while balance > 0:
    balance = a
    for month in range(1, 13):
        unpaidBalance = balance - minimumPaid
        interest = annualInterestRate / 12.0 * unpaidBalance
        balance = unpaidBalance + interest
    minimumPaid += 10

print ('Lowest Payment: ' + str(minimumPaid - 10))