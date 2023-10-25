class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_at_beginning(self):
        if not self.head:
            print("List is empty")
            return
        self.head = self.head.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()

num_elements = int(input("Enter the number of elements to insert at the beginning: "))
for i in range(num_elements):
    data = int(input(f"Enter element {i + 1}: "))
    ll.insert_at_beginning(data)

ll.display()
print("After deleting from beginning")
ll.delete_at_beginning()
ll.display()
