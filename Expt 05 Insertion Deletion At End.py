MAX_SIZE = 100

arr = [0] * MAX_SIZE
size = 0

n = int(input("Enter the number of initial elements: "))
elements = list(map(int, input("Enter the elements separated by spaces: ").split()))

for i in range(n):
    arr[i] = elements[i]
    size += 1

choice = int(input("Enter 1 to insert an element or 2 to delete an element: "))

if choice == 1:
    element = int(input("Enter the element to insert: "))
    if size < MAX_SIZE:
        arr[size] = element
        size += 1
    else:
        print("Overflow condition: Array is full, cannot insert.")
elif choice == 2:
    if size > 0:
        size -= 1
    else:
        print("Underflow condition: Array is empty, cannot delete.")

print("Array contents after the operation:")
for i in range(size):
    print(arr[i], end=" ")
