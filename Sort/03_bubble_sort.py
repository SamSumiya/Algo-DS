'''
    Bubble Sort

    approach: iteration 

        compare the first element with the rest of the element
        the key is that we will need to compare the entire list until i is at the last element and j 
        however, j which is in the nested loop should always start from 0 and the length of this is should be 
        i length less because the biggest number will go to the end. 



'''



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