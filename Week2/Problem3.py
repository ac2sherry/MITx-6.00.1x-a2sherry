def remainBalance(balance,annualInterestRate,minimumPayment,month = 12):
    remainingBalance = (1+annualInterestRate/12)*(balance-minimumPayment)
    if month == 1:
        return remainingBalance
    else:
        return remainBalance(remainingBalance,annualInterestRate,minimumPayment,month-1)
 

balance = 320000
annualInterestRate = 0.2
payment_min = 0
payment_max = balance
while True:
    payment = (payment_min + payment_max) / 2
    rB = remainBalance(balance,annualInterestRate,payment)
    if abs(rB) < 1e-6:
        break
    elif rB > 0: # payment too low
        payment_min = payment
    else:        # payment too high
        payment_max = payment

print("Lowest Payment: "+str(round(payment,2)))