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

print("Stack Before Popping:")
current = stack.top
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

popped_item = stack.pop()
if popped_item is not None:
    print("Popped:", popped_item)
else:
    print("Stack is empty.")
