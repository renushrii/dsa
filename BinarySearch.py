def BinarySearch(array, ele, i, j):
    while i <= j:
        mid = i + (j - i)//2

        if array[mid] == ele:
            return mid

        if array[mid] < ele:
            i = mid + 1

        else:
            j = mid - 1

    return -1


array = [3, 4, 5, 6, 7, 8, 9]
ele = 8
result = BinarySearch(array, ele, 0, len(array)-1)
if result == -1:
    print("Not Found")
else:
    print("element present on index: " +str(result))



