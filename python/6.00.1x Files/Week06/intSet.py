class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'


    def intersect(self,other):
        newSet=intSet()

        if len(other.vals)==0 and len(self.vals)==0:
            return newSet
                    
        for i in self.vals:
            if other.member(i):
                newSet.insert(i)

        return newSet                


    def __len__(self):
        """Returns the length of the set.
           This method is called by the `len` built-in function."""
        return len(self.vals)
        
        
i1=intSet()
i1.vals=[]
i1.insert(5)
i1.insert(3)
i1.insert(1)
i1.insert(7)
i1.insert(8)
i2=intSet()
print i1.intersect(i2)
