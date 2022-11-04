'''
    Two Sum 

    Approch: array 
        iterate through the list
        we will use target - current number to get the difference
        and we will find if the list has the element of difference
        if it does and it is not on the same index of the current index
        then we know the sum must equal to the target 
        so we can return the current index and the index of the element on the list 
        ** it won't work well with sorted list [0,0,1,2] 0 
        lets say the diff is 0 
        so we know that the current idx is 0 and the since list.index(el) will be 0, 
        the loop will go on to the next one, 
        and then we will finally get the result but it will be [1,0]
        we can sort this list but it will make the algorithm slow O(nlogn) 
    
    Approach: hashmap
        similar approach
        We will loop through the list and get diff 
        we will store the value and index in a hashmap 
        and then we will check if the diff is in the hashmap or not
        if it does, we will return the current idx and the index in hashmap hashmap[diff] 

        




'''



from typing import List


def twoSum_array(nums: List[int], target: int) -> List[int]:
    
    for idx, el in enumerate(nums): 
        diff = target - el
        if diff in nums and idx != nums.index(diff): 
            return [idx, nums.index(diff)]

def twoSum_hashmap(nums: List[int], target: int) -> List[int]:
        hashmap = {} 
        
        for idx, el in enumerate(nums): 
            diff = target - el
            if diff in hashmap: 
                return [hashmap[diff], idx]
            hashmap[el] = idx
            