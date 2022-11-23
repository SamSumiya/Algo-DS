'''

35. Search Insert Position
''' 
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right: 
            mid = left + (right - left) // 2

            if nums[mid] == target: 
                return mid
            elif nums[mid] > target:
                print(mid, right)
                right = mid - 1
                print(right)
            else: 
                left = mid + 1
        return left