'''

    Two Number Sum

    approach: hashset
        
        loop through the array
        we will keep adding each element to the hashset and move on to the next element
        also we will get the difference from the current element to subtract the target
        if hashset has it and the index does not equal to the index in the array (hashset allows us to have O(1) time complexity)
        then we can return the index 

        let say [1,2,1] and the target is 2
        
        {1}
        diff = 2 - 1 
        if hashset has 1 (True) and array.index(diff) != index (0 != 0) False
                                    this will be true when it goes to the last element which is 2
            then we will return [index, array.index(diff)]


'''

def twoNumberSum(array, targetSum):
    # if array == []: return array
    hashset = set(array)
    
    for idx, num in enumerate(array):
        diff = targetSum - num
        if diff in hashset and idx != array.index(diff): 
            return [array[array.index(diff)], array[idx]]
        hashset.add(diff)

    return [] 
