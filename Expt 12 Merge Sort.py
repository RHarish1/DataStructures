def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))

list_length = int(input("Enter the length of the list: "))
my_list = [ ]
for i in range(list_length):
    element = int(input(f"Enter element {i + 1}: "))
    my_list.append(element)
print("Before sorting")
print(my_list)
print("After Sorting")
merge_sort(my_list)
print(my_list)