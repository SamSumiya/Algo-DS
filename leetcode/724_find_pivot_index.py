
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        left_sub_sum = 0

        for idx, n in enumerate(nums):
            total_sum -= n
            if left_sub_sum == total_sum:
                return idx
            left_sub_sum += n

        return -1


nums = [2, 1, -1]
s = Solution()
r = s.pivotIndex(nums)
print(r)
