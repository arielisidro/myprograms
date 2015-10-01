def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    # Your code here
    if aStr=='':
        return 0
        
    return lenRecur(aStr[:-1])+1
    
print lenRecur('1')