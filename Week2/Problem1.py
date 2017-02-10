def PayingDebtoff(month,balance,annualInterestRate,monthlyPaymentRate):
    remainingBalance = (1+annualInterestRate/12)*(balance*(1-monthlyPaymentRate))
    if month == 1:
        return remainingBalance
    else:
        return PayingDebtoff(month-1,remainingBalance,annualInterestRate,monthlyPaymentRate)
    

#balance = 484
#annualInterestRate = 0.2
#monthlyPaymentRate = 0.04

rB = PayingDebtoff(12,balance,annualInterestRate,monthlyPaymentRate)
print("Remaining balance: "+str(round(rB,2)))