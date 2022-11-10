
'''
    Sorted Square Array


    Approach: O(nlogn) time complexity
        iterate througth the array and reassign or add value to a new list
        for input that has negative values such as 
        [-3, -2, -1] it will be [9,4,1] so we can use sort to get the right order
        [-5, 0, 5] it will be [25, 0, 25] and sort will work again
    
    Approach: O(n) time complexity

        this is a bit more advanced approach
        we can create a new array with values 0 by [ o for _ in arr]
        then get the first idx and last idx 
        
        then we can make a comparison between first and last element
        if the abs(first) is greater then abs(last)
        then we can replace the first * first to the idx (this idx must be from the last idx)
            reason: if we have a list [-6, 0, 5] and we add each value to the first idx 
            then we will have [36, 25, 0]
        

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





array = [-2, 0, 5, 10]

r = sortedSquaredArray(array)
print(r)