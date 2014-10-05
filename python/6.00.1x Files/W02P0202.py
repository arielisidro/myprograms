balance=3926
unpaidBalance=balance
annualInterestRate=0.2
monthlyPayment=0.0
while unpaidBalance>0:
    unpaidBalance=balance
    monthlyPayment+=10
    for month in range(1,13):
        unpaidBalance-=monthlyPayment
        unpaidBalance+=unpaidBalance * annualInterestRate / 12
print 'Lowest Payment: '+str(int(monthlyPayment))
