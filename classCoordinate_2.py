class Point(object):
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
        
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
        
    def __mul__(self, other):
        '''override what the operator * does 
        if both the left and right operands of * are Point type.'''
        return Point(self.x * other.x, self.y * other.y)
        
    def __rmul__(self, other):
        '''override what the operator * does
        if the left operand of * is a primitive type, i.e. int
        and the right operand of * is a Point type.'''
        return Point(other * self.x, other * self.y)
        # test sample
        # >>> p1 = Point(3, 4)
        # >>> print 2 * p1



def multadd(x, y ,z):
    '''args can be numeric values, i.e. int, float
    and also can be class objects if * operator has been defined
    by methods like __mul__() and __rmul__().'''
    return x * y + z
        
# Test Sample
p1 = Point(3, 4)
p2 = Point(5, 8)
p3 = Point(12, 1)
# print multadd(p1, p2, p3)
# print multadd(2, p2, p3)