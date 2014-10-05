def gcdIter(a,b):

    testValue=min(a,b)

    while not(a%testValue==0 and b%testValue==0):
        testValue-=1            

    return testValue
    
def gcdRecur(a,b):

    print str(a)+str(b)
    if b==0:
        return a

    return gcdRecur(b,a%b)
    
a=int(raw_input('a : '))
b=int(raw_input('b : '))

print 'gcd: '+str(gcdIter(a,b))
print 'gcd: '+str(gcdRecur(a,b))
