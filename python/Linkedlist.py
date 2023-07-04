class Node:
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

  
    def __repr__(self):
        '''
        Return a string representation of the list 
        Takes O(n)
        '''
        return "<Node data %s>" %self.data
