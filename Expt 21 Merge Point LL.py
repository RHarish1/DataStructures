
class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def find_intersection(headA, headB):
    if not headA or not headB:
        return None

    tailA, tailB = headA, headB

    while tailA.next:
        tailA = tailA.next
    while tailB.next:
        tailB = tailB.next

    if tailA != tailB:
        return None

    tailA, tailB = headA, headB

    while tailA != tailB:
        tailA = tailA.next
        tailB = tailB.next

    return tailA

list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(3)

list2 = Node(4)
list2.next = Node(5)
list2.next.next = list1.next.next

intersection_node = find_intersection(list1, list2)

if intersection_node:
    print("Input:")
    print("List 1: 1 -> 2 -> 3")
    print("List 2: 4 -> 5 -> 3 (Intersection here)")
    print("\nOutput:")
    print(f"Intersection node value: {intersection_node.val}")
else:
    print("Input:")
    print("List 1: 1 -> 2 -> 3")
    print("List 2: 4 -> 5")
    print("\nOutput:")
    print("No intersection found")
