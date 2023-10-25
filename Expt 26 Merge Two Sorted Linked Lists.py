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

def merge_sorted_lists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    result = LinkedList()
    current1 = list1.head
    current2 = list2.head

    while current1 and current2:
        if current1.data < current2.data:
            result.append(current1.data)
            current1 = current1.next
        else:
            result.append(current2.data)
            current2 = current2.next

    while current1:
        result.append(current1.data)
        current1 = current1.next

    while current2:
        result.append(current2.data)
        current2 = current2.next

    return result

list1 = LinkedList()
list2 = LinkedList()

list1.append(1)
list1.append(3)
list1.append(5)

list2.append(2)
list2.append(4)
list2.append(6)

def display_linked_list(linked_list):
    node = linked_list.head
    while node:
        print(node.data, end=" -> ")
        node = node.next
    print("None")

print("Original List 1:")
display_linked_list(list1)

print("Original List 2:")
display_linked_list(list2)

merged_list = merge_sorted_lists(list1, list2)

merged_node = merged_list.head
print("\nMerged Sorted Linked List:")
display_linked_list(merged_list)

