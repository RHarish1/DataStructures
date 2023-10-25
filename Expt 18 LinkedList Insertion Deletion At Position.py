class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_position(self, data, position):
        if position < 0:
            print("Invalid position. Please enter a non-negative position.")
            return
        if position == 0:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        new_node = Node(data)
        current = self.head
        for i in range(position - 1):
            if not current:
                print("Position not found in the list. Please choose a valid position.")
                return
            current = current.next
        if not current:
            print("Position not found in the list. Please choose a valid position.")
            return
        new_node.next = current.next
        current.next = new_node

    def delete_at_position(self, position):
        if not self.head:
            print("List is empty.")
            return
        if position == 0:
            self.head = self.head.next
            return
        current = self.head
        for i in range(position - 1):
            if not current.next:
                print("Position not found in the list. Please choose a valid position.")
                return
            current = current.next
        if not current.next:
            print("Position not found in the list. Please choose a valid position.")
            return
        current.next = current.next.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

ll = LinkedList()

position = int(input("Enter the position to insert an element: "))
data = int(input(f"Enter the element to insert at position {position}: "))
ll.insert_at_position(data, position)
print("Linked List after insertion:")
ll.display()

position_to_delete = int(input("Enter the position to delete an element: "))
ll.delete_at_position(position_to_delete)
print("Linked List after deletion:")
ll.display()
