'''
    Product Except Self

    this is also a part of arrays and hashing problem sets

    given a list that contains numbers
    we should return a new list of numbers that are multiplied with every other numbers but itself
    lets say if the list is 
    [2, 3, 5]
    the first number should be 15: 3 * 5
    the second number should be 10: 2 * 5
    the last number should be 6: 2 * 3 

    approach: iteration prefix and postfix
        we can get two sets of list that contains prefixes and postfixes
        the way to get it multiply the first number with the previos multiplied result
        for the first number, since there is nothing in front of it we can use 1
        prefix will go from the beginning and postfix will go from the end

        once we have the correct collections of numbers
        we can iterate through the lists 
        for first number, we will still run into issue that there is nothing before it
        we can still use 1 as a placeholder and set the index as -1
        since it will be in the same loop to check conditions
        we have to be careful with the value -1 in else statement, 
        we can use elif to avoid when it is -1 or 
        else and if to avoid the issue there 
    

'''

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        postfix = [] 
        output = [] 
        i = 0
        j = len(nums) - 1
        while i < len(nums):
            if len(prefix) == 0:
                prefix.append(nums[i] * 1)
            else: 
                prefix.append(nums[i] * prefix[i-1])
            
            i += 1 
        k = -1 
        while j >= 0: 
            if len(postfix) == 0: 
                postfix.append(nums[j] * 1)
            else:
                postfix.append(nums[j] * postfix[k])
            
            j -= 1
            k += 1 
        
        l = -1
        m = len(postfix) - 2
        
        while l < len(prefix) - 1:
            if l == -1: 
                output.append(1 * postfix[m]) 
            if m == -1: 
                output.append(1 * prefix[l]) 
            else :
                if l > -1: 
                    output.append(prefix[l] * postfix[m])
            m -= 1
            l += 1 
        
        return output