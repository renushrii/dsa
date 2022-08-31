import random
def QuickSort(array, left, right):
    if len(array[left:right]) <= 1:
        return

    pivot_index = random.randrange(left, right)
    #print(f"{array[pivot_index]} --> {array[left:right]} | ({left},{right})")
    i = left
    j = right-1
    array[pivot_index], array[j] = array[j], array[pivot_index]
    j = j -1
    while i < j:
        if array[i] <= array[right-1]:
            i += 1
            continue

        array[i], array[j] = array[j], array[i]
        j -= 1

    #print(array)
    if array[i] <= array[right-1]:
        i += 1
    array[i], array[right-1] = array[right-1], array[i]
    #print(array)

    if left < i:
        QuickSort(array, left, i)
    if i +1 < right:
        QuickSort(array, i+1, right)


array = [5,7,45,89,0,34,56,67,3,22,33,24,34]
QuickSort(array, 0, len(array))
print(array)


    






        



