class Queue(object):

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        self.vals.append(e)

    def remove(self):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            removed=self.vals[0]
            self.vals.remove(self.vals[0])
            return removed
        except:
            raise ValueError()

    def __str__(self):
        """Returns a string representation of self"""
        return '{' + ','.join([str(e) for e in self.vals]) + '}'


q1 = Queue()
q2 = Queue()
q1.insert(17)
q2.insert(20)
q1.remove()
q2.remove()