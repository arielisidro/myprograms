# -*- coding: utf-8 -*-
class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        self.before = before
    def setAfter(self, after):
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name
        
def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.    
    """
    # Your Code Here
    temp=atMe
    while True:
        
        if newFrob.myName()>=temp.myName():
            if temp.getAfter()==None:
                temp.setAfter(newFrob)
                newFrob.setBefore(temp)
                break
            else:                    
                temp=temp.getAfter()
        else:
            if temp.getBefore()==None:
                temp.setBefore(newFrob)
                newFrob.setAfter(temp)
                break
                
            elif newFrob.myName()>=temp.getBefore().myName() and newFrob.myName()<=temp.myName():
                newFrob.setAfter(temp)
                newFrob.setBefore(temp.getBefore())
                temp.getBefore().setAfter(newFrob)
                temp.setBefore(newFrob)
                break
                
            else:
                temp=temp.getBefore()                

def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    # Your Code Here
    if start.getBefore()==None:
        return start

    return findFront(start.getBefore())                
                
    
            

eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')
ariel=Frob('ariel')
aei=Frob('aei')
print eric.myName()
print andrew.myName()
print ruth.myName()
print fred.myName()
print martha.myName()
#insert(eric, andrew)
#insert(eric, fred)
#insert(eric, aei)
#insert( andrew,ruth)
#insert(ruth, martha)
#insert(ruth,ariel)

print "Front: ",findFront(ruth).myName()


"""
"""