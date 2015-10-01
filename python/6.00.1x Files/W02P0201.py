balance=4842
annualInterestRate=.2
monthlyPaymentRate=.04

totalPaid=0.0

for month in range(1,13):
    
    print 'Month: '+str(month)
    
    minimumMonthlyPayment=round(balance*monthlyPaymentRate,2)
    remainingBalance=balance-minimumMonthlyPayment
    interest=round(annualInterestRate/12*remainingBalance,2)
    balance=remainingBalance+interest
    totalPaid+=minimumMonthlyPayment
    
    print 'Minimum monthly payment : '+str(minimumMonthlyPayment)
    print 'Remaining Balance: '+str(balance)
    
print '\nTotal paid: '+str(totalPaid)    
print 'Remaining Balance: '+str(balance)

