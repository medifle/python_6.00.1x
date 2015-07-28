import math

class Coordinate(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"
        
    def distance(self, other):
        return math.sqrt(pow((self.x - other.x), 2) + pow((self.y - other.y), 2))