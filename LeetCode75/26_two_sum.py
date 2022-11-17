class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        pairs = {}

        for idx, val in enumerate(nums):
            diff = target - val
            if diff in pairs:
                return [pairs[diff], idx]

            pairs[val] = idx
        return 