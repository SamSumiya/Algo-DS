class Solution(object):
    def search_iter(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target not in nums:
            return -1
        if nums[len(nums) // 2] == target:
            return len(nums) // 2
        elif nums[len(nums)//2] < target:
            return len(nums) // 2 + self.search(nums[len(nums)//2:], target)
        elif nums[len(nums) // 2] > target:
            return self.search(nums[:len(nums) // 2], target)

    def search_recur(self, nums, target):
        if target not in nums:
            return -1
        if nums[len(nums) // 2] == target:
            return len(nums) // 2
        elif nums[len(nums)//2] < target:
            return len(nums) // 2 + self.search(nums[len(nums)//2:], target)
        elif nums[len(nums) // 2] > target:
            return self.search(nums[:len(nums) // 2], target)


nums = [3, 4, 5, 6, 7, 8, 9]
x = 8
so = Solution()
r = so.search(nums, x)

print(r)
