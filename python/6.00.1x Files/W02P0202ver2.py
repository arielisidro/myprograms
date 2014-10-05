balance=999999
annualInterestRate=0.2

def computeBalance(balance,monthlyPayment):
    for month in range(1,13):
        balance-=monthlyPayment
        balance+=balance * annualInterestRate / 12
    return balance        

count=0
monthlyPayment=0.0
while computeBalance(balance,monthlyPayment)>0:
    count+=1
    monthlyPayment+=10

print 'Lowest Payment: '+str(int(monthlyPayment))
print count
    
    