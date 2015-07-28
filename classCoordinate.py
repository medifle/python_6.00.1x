import math

class Coordinate(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"
        #if __str__() is not defined but __repr__() is, then __repr() can also be used just like __str__()
        #try this by deleting definition of __str__(), and try to print a instance of Coordinate
        
    def distance(self, other):
        return math.sqrt(pow((self.x - other.x), 2) + pow((self.y - other.y), 2))

    def __repr__(self):
        return 'Coordinate(x=%r, y=%r)' % (self.x, self.y)
        #try to type the name of the instance of Coordinate and hit enter