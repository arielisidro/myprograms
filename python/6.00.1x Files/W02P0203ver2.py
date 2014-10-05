balance=999999
annualInterestRate=0.2

monthlyInterestRate=annualInterestRate/12.0

lowerBound=balance/12.0
upperBound=(balance * (1 + monthlyInterestRate)**12)/12.0

epsilon=.05
count=0

def computeBalance(balance,monthlyPayment):
    for month in range(1,13):
        balance -= monthlyPayment
        balance += balance * annualInterestRate / 12.0
    return balance        
    
def computeMonthlyPayment(lowerBound,upperBound):
    
    return round((lowerBound+upperBound)/2.0,2)
    

while True:
    count+=1
    monthlyPayment=computeMonthlyPayment(lowerBound,upperBound)
    unpaidBalance=computeBalance(balance,monthlyPayment)

    print unpaidBalance
    if abs(unpaidBalance)<epsilon:
        break       
    elif unpaidBalance<0:
        upperBound=monthlyPayment
    else:
        lowerBound=monthlyPayment        
            
print 'Lowest Payment: '+str(monthlyPayment)
print count