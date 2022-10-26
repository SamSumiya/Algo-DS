'''
    Subset of Arrays and Hashing
    
    https://leetcode.com/problems/contains-duplicate/submissions/ 

    approach: hashmap 
        create a empty hashmap
        populate hashmap with each number as key and value will be incremented as encouter
        if at any point the value is greater that 0 
        we know that there must be more than one same element
        so we can return True
        or return False at the end
'''


def containsDuplicate(nums):
    hashmap = {}

    for el in nums:
        if el not in hashmap:
            hashmap[el] = 0
        else:
            hashmap[el] += 1
        if hashmap[el] > 0:
            return True
    return False



nums = [1, 2, 3, 4]
r = containsDuplicate(nums)
print(r)