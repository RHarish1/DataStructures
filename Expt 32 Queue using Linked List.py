class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.is_empty():
            item = self.front.data
            self.front = self.front.next
            return item

    def is_empty(self):
        return self.front is None

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue Before Dequeue:")
current = queue.front
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

dequeued_item = queue.dequeue()
if dequeued_item is not None:
    print("Dequeued:", dequeued_item)
else:
    print("Queue is empty.")
