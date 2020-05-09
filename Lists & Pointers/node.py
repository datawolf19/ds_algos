class Node:
    def __init__(self, data=None):
        self.data = data 
        # Stores the reference to the next
        # Node.
        self.next = None 

    def __str__(self):
        return str(self.data)