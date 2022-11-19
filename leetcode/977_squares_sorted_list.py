'''
977. Squares of a Sorted Array

'''

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        left, right = 0, len(nums) - 1 
        output = [] 

        while left <= right: 
            left_num = nums[left] * nums[left]
            right_num = nums[right] * nums[right]

            if left_num > right_num: 
                output.append(left_num)
                left += 1
            else: 
                output.append(right_num) 
                right -= 1
        
        return output[::-1]
