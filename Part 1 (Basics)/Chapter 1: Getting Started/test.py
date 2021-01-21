print("Hello LinkedList")

class Node:
    def __init__(self, val = None, next = None):
        self.val = val
        self.next = next

class Linkedlist:
    def __init__(self):
        self.head = None

n1 = Node(2)
n2 = Node(3)

ll = Linkedlist()
n1 = ll.head