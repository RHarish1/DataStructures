class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node

    def reverseList(self):
        if self.head is None or self.head.next is None:
            return

        current = self.head
        prev = None
        Next = self.head.next

        while Next is not None:
            current.next = prev
            prev = current
            current = Next
            Next = current.next

        current.next = prev
        self.head = current

    def display(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()
elements = [1, 2, 3, 4, 5]

for element in elements:
    ll.insert_at_beginning(element)

print("Original Linked List:")
ll.display()

ll.reverseList()
print("\nReversed Linked List:")
ll.display()
