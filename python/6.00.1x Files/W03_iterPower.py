def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp<0:
        print ('exp must be an integer greater than or equal to zero')
        return 'error'
    else:
        power=1
        if exp>0:
            while exp>0:
                power=power*base
                exp -= 1
    return power            
            
def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp==0:
        return 1

    return base*recurPower(base,exp-1)
                        
def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    # Your code here
    if exp==0:
        return 1
    elif exp%2==0:
        return recurPowerNew(base*base,exp/2)
    return base*recurPowerNew(base,exp-1)

base=int(raw_input('base : '))
exp=int(raw_input('exp  : '))
print 'iterative power('+str(base)+','+str(exp)+')='+str(iterPower(base,exp))
print 'recursive power('+str(base)+','+str(exp)+')='+str(recurPower(base,exp))
print 'recur new power('+str(base)+','+str(exp)+')='+str(recurPowerNew(base,exp))
