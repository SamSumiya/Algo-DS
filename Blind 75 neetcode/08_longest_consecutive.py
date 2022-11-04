'''
    Longest Consecutive

    Approach: iteration and hashset
        convert the list into a hashset and loop through it
        we will try to find if there is a current num - 1 in the hashset
        if it does not, we can use a new var length and add one to it to match if there is a number that will match the current num -1 +1
        which if should have, then we can add 1 to the longest streak variable
        if it has current - 1, we will just keep moving to the point where current - 1 do longer exist. 


'''

from typing import List


def longestConsecutive(nums: List[int]) -> int:
        sets = set(nums)
        longest_seq = 0 
        
        for el in sets: 
            left_val = el - 1
            if left_val not in sets:
                length = 0 
                while el + length in sets: 
                    length += 1
                longest_seq = max(length, longest_seq)
        
        return longest_seq

nums = [100,4,200,1,3,2] 
r = longestConsecutive(nums)
print(r)