def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

list_length = int(input("Enter the length of the list: "))
my_list = [ ]
for i in range(list_length):
    element = int(input(f"Enter element {i + 1}: "))
    my_list.append(element)
print("Before sorting")
print(my_list)
print("After Sorting")
quick_sort(my_list)
print(my_list)