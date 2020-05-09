# Singly Linked List
# Has only one pointer b/t two successive nodes.
# Traversed in one direction.
# First to last but not reversed.

from node import Node

n1 = Node('eggs')
n2 = Node('ham')
n3 = Node('spam')

n1.next = n2
n2.next = n3 

current = n1 
while current:
    print(current.data)
    current = current.next

# Not a great implementation bc it reqs
# too much manual work, error-prone, 
# too much inner workings exposed to 
# programmer.