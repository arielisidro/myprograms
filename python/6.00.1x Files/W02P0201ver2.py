balance=4842
annualInterestRate=.2
monthlyPaymentRate=.04

totalPaid=0.0

def computeMonthly(balance,monthlyPaymentRate):
    return round(balance*monthlyPaymentRate,2)
    
def computeInterest(balance,annualInterestRate):
    return round(annualInterestRate/12*balance,2)
    
for month in range(1,13):
    
    print 'Month: '+str(month)
    
    minimumMonthlyPayment=computeMonthly(balance,monthlyPaymentRate)

    balance -= minimumMonthlyPayment
    balance += computeInterest(balance,annualInterestRate)
    
    totalPaid+=minimumMonthlyPayment
    
    print 'Minimum monthly payment : '+str(minimumMonthlyPayment)
    print 'Remaining Balance: '+str(balance)
    
print '\nTotal paid: '+str(totalPaid)    
print 'Remaining Balance: '+str(balance)

