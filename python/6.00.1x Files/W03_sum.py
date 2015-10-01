def sum(x):
    print x
    if x==0:
        return 0
    return x+sum(x-1)
    
x=int(raw_input('x: '))
print 'sum: '+str(sum(x))
                    