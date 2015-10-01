def f(x):
    step=0
    for i in range(1000):
        step+=1
        ans=i
    for i in range(x):
        ans+=1
    y=0
    z=0
    for i in range(x):
        y+=1
        
        for j in range(x):
            ans+=1
            z+=1

    print step
    print "y:",y,"z: ",z
    return            
        
        