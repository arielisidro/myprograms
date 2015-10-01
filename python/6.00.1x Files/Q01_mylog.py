
    
def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    if x<0:
        print 'x must be a positive integer'
        return 'Error'
    if b<2:
        print 'b must be greater than or equal to 2'
        return 'Error'                    
    
    largest_power=1
    l=0
    while l<=x:
        pow=power(b,l)
        #print pow
        if pow>largest_power:
            if pow<=x:
                largest_power=pow
            else:
                break
        l+=1 
    return l-1        
            
def power(base,p):
    if p==0:
        return 1
    return power(base,p-1)*base        
        
    

x=15
b=2
print myLog(x,b)

#print power(0,0)