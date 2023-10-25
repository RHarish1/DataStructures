def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
list_length = int(input("Enter the length of the list: "))
my_list = [ ]
for i in range(list_length):
    element = int(input(f"Enter element {i + 1}: "))
    my_list.append(element)
print("Before sorting")
print(my_list)
print("After Sorting")
selection_sort(my_list)
print(my_list)