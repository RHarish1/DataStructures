def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i] #Selecting the pivot for the code to run
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

list_length = int(input("Enter the length of the list: "))
my_list = [ ]
for i in range(list_length):
    element = int(input(f"Enter element {i + 1}: "))
    my_list.append(element)
print("Before sorting")
print(my_list)
print("After Sorting")
insertion_sort(my_list)
print(my_list)
