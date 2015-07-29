class IntSet(object):
    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self"""
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """
        Assumes e is an integer
        Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """
        Assumes e is an integer and removes e from self
        Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + 'not found')

    def getMembers(self):
        """Returns a list containing the elements of self.
        Nothing can be assumed about the order of the elements"""
        return self.vals[:]

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        #result = ''
        #for e in self.vals:
        #    result = result + str(e) + ','
        #return '{' + result[:-1] + '}' #-1 omits trailing comma
        # or you could use
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
        
    def intersect(self, other):
        '''Returns a new IntSet containing elements that appear in both sets.
        'other' should also be a instance of IntSet'''
        # initialize a new set
        commonValueSet = IntSet()
        # insert common values into the new set
        for e in self.vals:
            if other.member(e):
                commonValueSet.insert(e)
        return commonValueSet
        
    def __len__(self):
        '''len(s) returns the number of elements in s, which is a instance of IntSet'''
        return len(self.vals)