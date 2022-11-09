from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        left_sum = 0
        right_sum = 0

        while left < right:
            left_sum += nums[left]
            right_sum += nums[right]

            if left_sum == right_sum:
                print(left_sum, right_sum, nums[left], left)
                return left + 1
            elif left_sum < right_sum:
                left += 1
            else:
                right -= 1
        return -1
