balance=320000
annualInterestRate=0.2

monthlyInterestRate=annualInterestRate/12.0

lowerBound=balance/12.0
upperBound=(balance * (1 + monthlyInterestRate)**12)/12.0
unpaidBalance=balance

epsilon=.1

while abs(unpaidBalance)>=epsilon:
    unpaidBalance=balance
    monthlyPayment=round((lowerBound+upperBound)/2.0,2)
    for month in range(1,13):
        unpaidBalance-=monthlyPayment
        unpaidBalance+=unpaidBalance * annualInterestRate / 12.0

    if unpaidBalance<0:
        upperBound=monthlyPayment
    else:
        lowerBound=monthlyPayment        
            
print 'Lowest Payment: '+str(monthlyPayment)
