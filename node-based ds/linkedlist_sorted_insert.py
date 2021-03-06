class Node:
    # Function to initialize the node object
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList:

    # Function to initialize head

    # def __init__(self):
    #     self.head = None

    def __init__(self, head=None):
        self.head = head

    # def sortedInsert(self, new_node):
    def sortedInsert(self, new_data):
        new_node = Node(new_data) 
        
        # Special case for the empty linked list
        if self.head is None:
            # new_node.next = self.head
            self.head = new_node
        # Special case for head at end
        elif self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            # Locate the node before the point of insertion
            current = self.head
            while current.next is not None and current.next.data < new_node.data:
            # while current.next and current.next.data < new_node.data:

                current = current.next
            # new_node.next = current.next
            current.next = new_node

            
    # Function to insert a new node at the begining
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node


    # Utility function to print the linked list
    def printList(self):
        temp = self.head
        while temp:
            print (temp.data, end=" ")
            temp = temp.next


llist = LinkedList()

# new_node = Node(5)
# llist.sortedInsert(new_node)
llist.sortedInsert(5)

# new_node = Node(7)
# llist.sortedInsert(new_node)
llist.sortedInsert(7)


# new_node = Node(3)
# llist.sortedInsert(new_node)
llist.sortedInsert(3)


# new_node = Node(1)
# llist.sortedInsert(new_node)
llist.sortedInsert(1)


# new_node = Node(9)
# llist.sortedInsert(new_node)
llist.sortedInsert(9)

print ("Created Linked List")

llist.printList()
