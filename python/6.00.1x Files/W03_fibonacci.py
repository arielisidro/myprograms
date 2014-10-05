def fib(x):    
    assert type(x)==int and x>=0
    if x==0 or x==1:
        return 1
    else:        
        return fib(x-1)+fib(x-2)
    
x=int(raw_input('x: '))
print 'f: '+str(fib(x))                    