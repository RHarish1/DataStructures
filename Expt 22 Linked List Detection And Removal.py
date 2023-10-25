class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False

def remove_cycle(head):
    if not head:
        return None

    slow = head
    fast = head
    cycle_found = False

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            cycle_found = True
            break

    if not cycle_found:
        return head

    slow = head
    while slow.next != fast.next:
        slow = slow.next
        fast = fast.next

    fast.next = None
    return head

list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(3)
list1.next.next.next = list1.next 

print("Original List 1:")
node = list1

has_cycle_result = has_cycle(list1)
print("Example 1 - Has Cycle:")
print(has_cycle_result)

list2 = Node(4)
list2.next = Node(5)
list2.next.next = Node(6)
list2.next.next.next = list2.next  

print("\nOriginal List 2:")
node = list2

list2 = remove_cycle(list2)

has_cycle_result = has_cycle(list2)
print("Example 2 - Remove Cycle and Check for Cycle:")
print(has_cycle_result) 
