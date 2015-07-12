# paying the minimum

balance = 4842
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
totalPaid = 0
for month in range(1, 13):
    minimumPayment = balance * monthlyPaymentRate
    unpaidBalance = balance - minimumPayment
    interest = annualInterestRate / 12.0 * unpaidBalance
    balance = unpaidBalance + interest
    totalPaid = totalPaid + minimumPayment
    print ('Month: ' + str(month))
    print ('Minimum monthly payment: ' + str(round(minimumPayment, 2)))
    print ('Remaining balance: ' + str(round(balance, 2)))

print ('Total paid: ' + str(round(totalPaid, 2)))
print ('Remaining balance: ' + str(round(balance, 2)))