'''
1480. Running Sum of 1d Array

Goal: return a list that each value is the sum of the previous nums' total sum
for instance [1,2,3,4] => [1,3,6,10]
there is nothing before 1, so it stays the same 
2 will add previous 1, so it becomes 3
3 will add previous 1 and 2, so it becomes 6 
4 will add previous 1,2,3, so it becomes 10 


approach:
    we can either use index and sum to added every element in the list and create a list 
    or 
    we can start at index 1 and added the previous value to index 1, 
    then we index 1 will be 3, 
    then we go to index 2 and added the previous value 3 to it, so it becomes 6
    ... 
'''

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        i = 1 

        while i < len(nums): 
            nums[i] += nums[i-1]
        
            i += 1
        return nums
        