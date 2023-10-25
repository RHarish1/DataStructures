def findFloor(arr, n, x):
    low = 0
    high = n - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= x:
            ans = arr[mid]
            low = mid + 1
        else:
            high = mid - 1
    return ans

def findCeil(arr, n, x):
    low = 0
    high = n - 1
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= x:
            ans = arr[mid]
            high = mid - 1
        else:
            low = mid + 1
    return ans

def findPeakElement(arr):
    start = 0
    n = len(arr)
    end = n + 1
    arr = [float('-inf')] + arr + [float('-inf')]

    while start <= end:
        mid = (end + start) // 2
        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid - 1
        elif arr[mid] > arr[mid - 1]:
            start = mid + 1
        else:
            end = mid - 1
    return 0

def findMin(arr):
    low = 0
    high = len(arr) - 1
    ans = float('inf')

    while low <= high:
        mid = (low + high) // 2
        if arr[low] <= arr[high]:
            ans = min(ans, arr[low])
            break
        if arr[low] <= arr[mid]:
            ans = min(ans, arr[low])
            low = mid + 1
        else:
            ans = min(ans, arr[mid])
            high = mid - 1
    return ans

list_length = int(input("Enter the length of the list: "))
my_list = []

for i in range(list_length):
    element = int(input(f"Enter element {i + 1}: "))
    my_list.append(element)

print("Ceiling of a number in the list:", findCeil(my_list, list_length, int(input("Enter a number to find the ceiling for: "))))
print("Floor of a number in the list:", findFloor(my_list, list_length, int(input("Enter a number to find the floor for: "))))
print("Index of a peak element in the list:", findPeakElement(my_list))
print("Minimum element in the list:", findMin(my_list))
