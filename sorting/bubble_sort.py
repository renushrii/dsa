def BubbleSort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j+1] = array[j+1], array[j]

array = [5,8,9,1,0,4,3,7]
BubbleSort(array)
print(array)