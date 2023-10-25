def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

list_length = int(input("Enter the length of the list: "))
my_list = [ ]
for i in range(list_length):
    element = int(input(f"Enter element {i + 1}: "))
    my_list.append(element)

print("Before sorting")
print(my_list)
print("After Sorting")
bubble_sort(my_list)
print(my_list)


