


def bubble_sort(array): 

    i = 0 
    size = len(array)

    while i < size:
        j = 0 
        while j < size - 1 - i: 
            if array[j] > array[j+1]: 
                current_max = array[j]
                array[j] = array[j+1]
                array[j+1] = current_max
            j += 1 
        i += 1 
    
    return array





array = [-2, 45, 0, 11, -9]
r = bubble_sort(array)
print(r)