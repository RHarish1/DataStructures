my_array = []

#Making a list of fixed size to check overflow in python as well

num_elements = int(input("Enter the number of initial elements: "))
for i in range(num_elements):
    element = int(input(f"Element {i + 1}: "))
    my_array.append(element)

def insert_element(arr, element, index):
    if index < 0 or index > len(arr):
        print("Index out of range (Overflow)")
    else:
        arr.insert(index, element)
        print("Element inserted at index", index)

def delete_element(arr, index):
    if index < 0 or index >= len(arr):
        print("Index out of range (Underflow)")
    else:
        deleted_element = arr.pop(index)
        print("Deleted element:", deleted_element)

# Get user input for insertion and deletion
insert_element(my_array, int(input("Enter element to insert: ")), int(input("Enter index to insert: ")))

delete_element(my_array, int(input("Enter index to delete: ")))

print("Updated Array:", my_array)
