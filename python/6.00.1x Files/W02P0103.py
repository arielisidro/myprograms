s = 'abcdebcdexfghijklmxyz'
length=len(s)
longest=''
for pos in range(length):
    index=pos
    string=s[index]
    while index<length-1:
        if s[index]<=s[index+1]:
            string+=s[index+1]
            index+=1
        else:
            break
    if len(string)>len(longest):
        longest=string
    if index>length-len(longest):
        break        
print 'Longest substring in alphabetical order is: '+longest                
        
