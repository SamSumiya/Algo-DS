'''
    26. Remove Duplicates from Sorted Array


Approach: 
    Since its a sorted list
    [1,1,2,2,3,5]

    we will need to make the list look like this
    [1,2,3,5,_,_]

    We will loop through the list and find if the current val is not equal to the next
    then we can update the current one to next one
    so we get [1,2,2,2,3,5]
    then next time we will update it to 
    [1,2,3,2,3,5]
    and 
    [1,2,3,5,3,5]

    It looks like we will just need to update from the first one to the last unique element
    so we can use an index to track from 0 to the last one

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
                print(nums)
                left += 1
            i += 1

        return left


input = [1,1,2,2,3,5]
su = Solution()

r = su.removeDuplicates(input)

print(r)