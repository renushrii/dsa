class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
            return 

        self.tail.next = Node(val)
        self.tail = self.tail.next





llist = linkedlist()
llist.insert(4)
llist.insert(9)
llist.insert(6)

