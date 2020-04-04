class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, new_data):
        if self.head is None:
            self.head = Node(new_data)
            return
        while self.head.next:
            self.head = self.head.next
        self.head.next = Node(new_data)

    def printList(self):
        while self.head:
            print(self.head.data, end=" "),
            self.head = self.head.next

l1 = LinkedList()

l1.append(3)
l1.append(5)
l1.append(7)
l1.append(9)
l1.append(11)

l1.printList()

# l2 = LinkedList()

# l2.append(3)

# l2.printList()

# print (l1.printList() == l2.printList())

# print(type(l1))

# a = Node(3)
# b = Node(3)

# print(a == b)



