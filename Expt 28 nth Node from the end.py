class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def find_nth_from_end(self, n):
        if not self.head:
            return None
        
        first_ptr = self.head
        second_ptr = self.head
        
        for _ in range(n):
            if first_ptr is None:
                return None  
            first_ptr = first_ptr.next

        while first_ptr:
            first_ptr = first_ptr.next
            second_ptr = second_ptr.next

        return second_ptr.data

linked_list = LinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)

def display_linked_list(linked_list):
    current = linked_list.head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

print("Original Linked List:")
display_linked_list(linked_list)

n = int(input("Enter the value of 'n' to find the nth node from the end: "))

nth_node = linked_list.find_nth_from_end(n)

if nth_node is not None:
    print(f"The {n}th node from the end is {nth_node}")
else:
    print(f"The linked list is shorter than {n} nodes.")
