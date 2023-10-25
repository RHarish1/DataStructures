class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def find_middle(self):
        slow_ptr = self.head
        fast_ptr = self.head

        while fast_ptr is not None and fast_ptr.next is not None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        return slow_ptr.data

ll = LinkedList()

# Add elements to the linked list
ll.head = Node(1)
ll.head.next = Node(2)
ll.head.next.next = Node(3)
ll.head.next.next.next = Node(4)
ll.head.next.next.next.next = Node(5)

curr=ll.head
while curr.next is not None:
    print(curr.data,"->",end="")
    curr=curr.next
print(curr.data)

# Find the middle element of the linked list
middle = ll.find_middle()

# Print the middle element
print("The middle element is:", middle)

