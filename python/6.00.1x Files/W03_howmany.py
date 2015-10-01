def howMany(aDict):

    count=0    
    for e in aDict.values():
        count+=len(e)
        
    return count
    
def biggest(aDict):
    
    if len(aDict)==0:
        return None
    
    biggestKey=aDict.keys()[0]
    biggestLen=len(aDict[biggestKey])
    
    for k in aDict.keys():
        
        if biggestLen<len(aDict[k]):
            biggestKey=k
            biggestLen=len(aDict[k])
        
    return biggestKey
    
    


animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')
#print howMany(animals)
print biggest(animals)

