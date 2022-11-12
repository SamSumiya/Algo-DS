'''
    26. Remove Duplicates from Sorted Array


'''


class Solution(object):
    def removeDuplicates(self, nums):
        """
            :type nums: List[int]
            :rtype: int
        """
        left = 1
        i = 0

        while i < len(nums)-1:
            if nums[i] != nums[i+1]:
                nums[left] = nums[i+1]
                left += 1
                i += 1

        return left
