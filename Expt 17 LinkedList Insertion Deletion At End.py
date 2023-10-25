class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_at_end(self):
        if not self.head:
            print("List is empty")
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()

num_elements = int(input("Enter the number of elements to insert at the end: "))
for i in range(num_elements):
    data = int(input(f"Enter element {i + 1}: "))
    ll.insert_at_end(data)

print("Linked List after insertion:")
ll.display()

ll.delete_at_end()
print("Linked List after deletion:")
ll.display()
