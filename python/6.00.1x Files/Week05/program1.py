def program1(L):
    a=0
    b=0
    c=0
    multiples = []
    c+=1
    for x in L:
        a+=1
        for y in L:
            b+=1
            multiples.append(x*y)
            b+=1
            b+=1

    print "a:",a,"b:",b
    return multiples

def program2(L):
    squares = []
    a=1
    b=0
    c=0
    
    for x in L:
        b+=1
        for y in L:
            c+=1
            c+=1
            if x == y:
                squares.append(x*y)
                c+=2
    a+=1
    print "a:",a,"b:",b,"c:",c
                    
    return squares    

def program3(L1, L2):
    intersection = []
    a=1
    b=0
    c=0
    for elt in L1:
        b+=1
        if elt in L2:
            c+=1
            intersection.append(elt)
            c+=1
    a+=1
    print "a:",a,"b:",b,"c:",c
            
    return intersection        