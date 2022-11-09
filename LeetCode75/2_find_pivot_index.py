'''

    Day 1 Q2

    This is an interesting question. In stead of using two pointers which is a useful technique for many cases. 
    This one actually should be solved in a different way. 
    Two pointer approach could work if the list is sorted instead of unsorted

    1,

        Goal:  
        the goal is to return the index where the first left half equals to the right half, 
        
        Approach: 
        in first glance, it looks like two pointers would be a good candidate for solving this challenge
        since we can iterate from the left and right side until the sum of those two equals to each other. 
        in this case [1,1,2] 
        left starts at index 0 and right starts at index 2
        if the left side is less than the right side, we will increment the index from 0 to 1 and get the sum again.
        if the left sum equals to right sum, 
        we will return the index which is 1

        However, for inputs like [2, 1, -1]
        we will need to move the left pointer to 1 instead of 0 
        or [2,1,1] we don't need to move the pointer. So it seems like the way to determine the index cannot be decided by the pointer. 

        so what is a generic solution for [2, 1, -1] and [2,1,1], the first one index will be 1 and second one will be 1
        the common thing for those two inputs is that the left side has to match the right side
        for the first input, it seems that the 2 is an obstacle so how can we remove the 2 and move on to the 1 without removing it from the list
        one thing we can do is to get the total sum of the list and use it to subtract 2 then we move on the [1, -1]
        then the remaining num is 1 and the value on index 1 is also 1
        so we know that the left side equals to the right size at index 0 then we will return 0 
''' 
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_total = 0 

        for idx, num in enumerate(nums): 
            total_sum -= num 

            if total_sum == left_total: 
                return idx 
            
            left_total += num 
        
        return -1
