def McNuggets1(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # Your Code Here
    if n<1:
        print "n must be greater than 0"
        return False
        
    package=(6+9+20,6+9,6+20,9+20,6,9,20)
    for p in package:
        if n%p==0:
            return True
            
    return False
    
def McNuggets(n):
    """
    n is an int

    Returns True if some integer combination of 6, 9 and 20 equals n
    Otherwise returns False.
    """
    # Your Code Here    
    for i in range (n):
        for j in range (n):
            for k in range (n):
                if i*6+j*9+k*20==n:
                    return True
    return False
     
def xyz(n):                                           
    packages=[6,9,20]
    def isCombination(n,packages):
        if n==0:
            return True
        elif n<0:
            return False
        elif len(packages)==0:
            return False
        else:
            return isCombination(n-packages[0],packages[1:])                        
        
    if n>0:
        return isCombination(n,packages)
    else:
        return False
        

for n in range(-1,40):
    print "n=",n,McNuggets(n)                    
       
