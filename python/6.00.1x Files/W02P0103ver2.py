s = 'abcdebcdexfghijklmxyz'
length=len(s)
longest=s[0]
current=s[0]
def checkLonger(longer,string2):

    if len(string2)>len(longer):
        longer=string2
        
    return longer        

for pos in range(1,length):
    print pos

    if s[pos]>=current[-1]:
        current+=s[pos]
    else:
        longest=checkLonger(longest,current)
        current=s[pos]
                
longest=checkLonger(longest,current)

    
print 'Longest substring in alphabetical order is: '+longest                
