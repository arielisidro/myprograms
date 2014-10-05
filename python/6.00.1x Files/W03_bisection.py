def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    middle=len(aStr)/2
    if len(aStr)==0:
        return False
    elif char==aStr[middle]:
        return True
    elif char<aStr[middle]:
        return isIn(char, aStr[:middle])
        
    return isIn(char,aStr[middle+1:])
    

print isIn('x','abcdefg')        
        
    
