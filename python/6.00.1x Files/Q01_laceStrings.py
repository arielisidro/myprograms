def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length, 
    then the extra elements should appear at the end.
    """
    # Your Code Here
    p=0
    s=''
    while p < min(len(s1),len(s2)):
        s+=s1[p]+s2[p]
        p+=1
    if len(s1)>len(s2):
        s+=s1[p:]
    elif len(s2)>len(s1):
        s+=s2[p:]
        
    return s
    
                                                    
            
print 'xxx'+laceStrings('abc','def')+'xxx'
print laceStrings('ab','def')
        