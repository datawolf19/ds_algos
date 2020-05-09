from node import Node 

class SinglyLinkedList:
    def __init__(self):
        self.tail = None 

    def append(self, data):
        # Encapsulate the data in a Node
        # A node has data and a reference to
        # the next node.
        
        node = Node(data)

        # An empty list's tail is set to None.
        # The tail is the first entry of a 
        # SLL.
        if self.tail == None:
            self.tail = node 
        else:
            # This has an O(n) complexity because
            # adding more elements to the list 
            # will take more time since it must
            # traverse the entire list to add 
            # the next node reference.
            current = self.tail
            while current.next:
                current = current.next
            current.next = node 


words = SinglyLinkedList()

words.append('egg')
words.append('ham')
words.append('spam')

current = words.tail
while current:
    print(current.data)
    current = current.next

class SinglyLinkedListFast:
    def __init__(self):
        # Lists now have a head (most recently added element)
        self.head = None
        # and the start of the list (tail)
        self.tail = None
        self.size = 0

    def append(self, data):
        # Nodes hold data and reference to 
        # the next node or None if at the end.
        node = Node(data)
        self.size += 1
        
        # Checks if there is a value for head.
        # If not then assign head & tail to node.
        # If a value of head exists then 
        if self.head:
            # Subsequent items are added here
            self.head.next = node
            # The head is set to the current 
            # reference. 
            self.head = node
        else:
            # First item is tail
            self.tail = node
            # Reference is set to first item
            self.head = node
    
    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    def delete(self, data):
        # Assign the memory location of 
        # self.tail to both current & prev
        current = self.tail 
        prev = self.tail 

        # List traversal
        while current:
            # Looking for data match
            if current.data == data:
                # What if the first entry
                # matches? The first entry
                # is set to the next entry.
                if current == self.tail:
                    self.tail = current.next
                else:
                    prev.next = current.next
                self.size -= 1
                return 
            prev = current 
            current = current.next 


chars = SinglyLinkedListFast()

for char in 'wolfgang':
    # Here 'w' would be set to tail
    # and 'g' would be set to head.
    chars.append(char)

current = chars.tail
while current:
    print(current.data)
    current = current.next