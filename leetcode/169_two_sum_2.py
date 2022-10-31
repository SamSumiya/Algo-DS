'''
    Two Sum 2
    given a sorted list return two index that the elements is 0 when sum them together

    approach: two pointer
        get the first idx and last idx
        before the two pointers intersect
        we will try to get the sum of those two numbers
        if the sum is greater than the target
        we shall move the last index to the -1 
        if the sum if less than the target
        we shall move the first index to +1
'''

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:        
        i, j = 0, len(numbers) - 1

        while i < j: 
            sum = numbers[i] + numbers[j]
            if sum == target: return [i+1, j+1]
            else: 
                if sum < target: 
                    i += 1
                else: 
                    j -= 1 
                    
        return [-1, -1]