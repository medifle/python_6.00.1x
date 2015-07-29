class Queue(object):
    def __init__(self):
        self.vals = []
        
    def insert(self, e):
        '''inserts one element in your Queue'''
        return self.vals.append(e)
        
    def remove(self):
        '''removes (or 'pops') the first element from your Queue and returns it.
        If the queue is empty, raises a ValueError.'''
        try:
            return self.vals.pop(0)
        except:
            raise ValueError
        