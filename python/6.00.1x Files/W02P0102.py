s = 'bobob'
count=0
for bob in range(len(s)-2):
    print s[bob:bob+3]
    if s[bob:bob+3]=='bob':
        count+=1
print 'Number of times bob occurs is: '+str(count)        