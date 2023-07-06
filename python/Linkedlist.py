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
''' 
N1 = Node(10)
print(N1)

N2 = Node(20)
print(N2)

N1.next_node = N2
print(N1.next_node)
'''
class Linkedlist:
    
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head == None

    def size(self):
        '''
        returns the number of nodes in the list
        takes O(n) time
        '''
        current = self.head
        count = 0

        # while current != None:
        while current:  
            count +=1
            current = current.next_node #will terminate when current.next_node at Null (tail)
        return count

    def add(self, data):
        '''
        Adds new Node containing data at head of the list
        takes O(1) time 
        '''
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        '''
        Search for the first node containing data that matches the key
        Returns the node or 'None' if not found
        Takes linear time or O(n)
        '''
        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None
            
    def insert(self, data, index):
        ''' 
        Inserts new Node containing data at index position
        Insertion takes constant time O(1), but 
        Finding the node at insertion point takes linear time O(n) time

        Takes overall Linear time O(n)
        '''
        if index == 0:
            self.add(data)
        if index > 0:
            new = Node(data)

            position = index
            current = self.head

        while position > 1:
            current = Node.next_node
            position -= 1

        prev_node = current
        next_node = current.next_node

        prev_node.next_node = new
        new.next_node = next_node
    
    def remove(self, key):
        '''
        Removes Node containing data that matches the key
        Returns node or None if key doesn't exist
        Takes O(n) time
        '''
        current = self.head
        previous = None
        found = False 

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
        
        return current
            

    def __repr__(self):
        '''
        Return a string representation of the list 
        Takes O(n)
        '''
        nodes = [ ]
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" %current.data)
            elif current.next_node == None:
                nodes.append("[Tail: %s]" %current.data)
            else:
                nodes.append("[%s]" %current.data)

            current = current.next_node
        return '-> '.join(nodes)

l = Linkedlist()
l.add(10)
print("size of linkedlist is: ", l.size())
print("adding 3 more nodes")
l.add(20)
l.add(30)
l.add(40)
print("size of linkedlist now is: ", l.size())
print(l)
n1 = l.search(15)
n2 = l.search(10)

print("first search: ", n1)
print("second search: ", n2)
    
