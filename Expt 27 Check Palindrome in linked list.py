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

    def is_palindrome(self):
        if not self.head:
            return True

        stack = []
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr and fast_ptr.next:
            stack.append(slow_ptr.data)
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next

        if fast_ptr:
            slow_ptr = slow_ptr.next

        while slow_ptr:
            if slow_ptr.data != stack.pop():
                return False
            slow_ptr = slow_ptr.next
        return True
    
def display_linked_list(linked_list):
    node = linked_list.head
    while node:
        print(node.data, end=" -> ")
        node = node.next
    print("None")
linked_list = LinkedList()

linked_list.append(1)
linked_list.append(2)
linked_list.append(3)
linked_list.append(2)
linked_list.append(1)

display_linked_list(linked_list)
is_palindrome = linked_list.is_palindrome()

if is_palindrome:
    print("The linked list is a palindrome.")
else:
    print("The linked list is not a palindrome.")
