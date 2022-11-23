'''


'''




from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1
        

        while left <= right:
            mid_point = left + (right - left) // 2
            if target == nums[mid_point]: 
                return mid_point
            elif target > nums[mid_point]:
                left = mid_point + 1
            else: 
                right = mid_point - 1
        
        return -1 
        