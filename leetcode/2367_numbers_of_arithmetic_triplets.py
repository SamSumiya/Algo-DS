'''
    2367. Number of Arithmetic Triplets



'''


from typing import List


class Solution:
    def arithmeticTriplets_pointers(self, nums: List[int], diff: int) -> int:
        output = 0
        i = 0
        size = len(nums) - 1

        while i < size:
            j = i + 1
            k = len(nums) - 1

            while j < k:
                if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                    output += 1
                    j += 1
                elif nums[j] - nums[i] < diff:
                    j += 1
                elif nums[k] - nums[j] < diff:
                    k -= 1
                elif nums[k] - nums[j] > diff:
                    k -= 1
                elif nums[j] - nums[i] > diff:
                    j += 1
            i += 1

        return output

    def arithmeticTriplets_sets(self, nums: List[int], diff: int) -> int:
        output = 0 
        seen = set()
        
        for n in nums: 
            if n - diff in seen and n - diff * 2 in seen:
                output += 1
            seen.add(n)
        
        return output


nums = [0,1,4,6,7,10]
diff = 3
s = Solution()
a = s.arithmeticTriplets_pointers(nums, diff)
b = s.arithmeticTriplets_sets(nums, diff)
print(a,b)