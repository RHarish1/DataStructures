#Using array
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Stack:", stack.items)
print("Pop:", stack.pop())
print("Size:", stack.size())

#Using linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if not self.is_empty():
            item = self.top.data
            self.top = self.top.next
            return item

    def is_empty(self):
        return self.top is None

stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print("Pop:", stack.pop())
