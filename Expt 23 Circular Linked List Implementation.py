class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def display(self):
        if not self.head:
            return
        temp = self.head
        while True:
            print(temp.val, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break

# Example usage:
cll = CircularLinkedList()

# Inserting elements into the circular linked list
cll.insert(1)
cll.insert(2)
cll.insert(3)

# Displaying the elements in the circular linked list
print("Circular Linked List:")
cll.display()
