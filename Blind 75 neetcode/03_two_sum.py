'''
    Subset of Arrays and Hashing
    https://leetcode.com/problems/two-sum/


    approachl: hashmap
        the key here is that we will always keep the previous value and idx in the hashmap 
        the value being the key and idx being the value
        so as we iterate through the list, 
        we can check if the different of target minus the current value is in the hashmap
        if it does
        then we can just return the idx in hashmap and the current idx

'''




from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {} 
        
        for idx, el in enumerate(nums): 
            diff = target - el
            if diff in hashmap: 
                return [hashmap[diff], idx]
            
            if el not in hashmap: 
                hashmap[el] = idx
            
        return 