def iterativePower(x,p):
    result=1
    for turn in range(p):
        result=result*x
    return result
        
    
x=int(raw_input('Enter a number: '))
p=int(raw_input('Enter an integer power: '))

print 'Answer : '+str(iterativePower(x,p))

result = 1
for turn in range(p):
    result=result*x
    print ('iteration: '+str(turn) + ' current results: '+str(result))
    
    
