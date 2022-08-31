def SelectionSort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i+1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        
        array[i], array[min_index] = array[min_index], array[i]

array = [3,7,8,4,5,0,2]
SelectionSort(array)
print(array)

    

            
