
'''
    Sorted Square Array


    Approach: O(nlogn) time complexity
        iterate througth the array and reassign or add value to a new list
        for input that has negative values such as 
        [-3, -2, -1] it will be [9,4,1] so we can use sort to get the right order
        [-5, 0, 5] it will be [25, 0, 25] and sort will work again
    
    Approach: O(n) time complexity
        

'''




def sortedSquaredArray(array):
    sorted_squares = [0 for _ in array]
    min_idx = 0 
    max_idx = len(sorted_squares) - 1 

    for idx in reversed(range(len(array))): 
        smaller_value = array[min_idx]
        larger_value = array[max_idx]

        if abs(smaller_value) > abs(larger_value): 
            sorted_squares[idx] = smaller_value * smaller_value 
            min_idx += 1
        else:
            sorted_squares[idx] = larger_value * larger_value 
            max_idx -= 1
    
    return sorted_squares





array = [-10, -5, 0, 5, 10]

r = sortedSquaredArray(array)
print(r)