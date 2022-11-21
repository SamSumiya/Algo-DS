from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        mid = len(nums) // 2
        counts = {} 
        op = 0 

        for val in nums: 
            if val not in counts: 
                counts[val] = 1
            else: 
                counts[val] += 1

        for ky, val in counts.items(): 
            if val > mid:
                op = ky
        
        return op 
