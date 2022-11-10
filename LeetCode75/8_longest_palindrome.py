'''
409. Longest Palindrome

Approach: 
    There are two ways to form a palindrome
    1. just even numbers
    2. even numbers with a odd number

    for cases like aabb, it is easy we can just return 4 
    but for cases like aaa, left is c, right is c and middle is c
    so we can return 3
    the trick here is that we don't need to add elements that is an odd number to its fullest.
    we can just add a even max to the count 
    cccaaa 
    so we can do 
    acaca
    or 
    caca

'''


class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        hashmap = {}
        count = 0

        for val in s:
            if val not in hashmap:
                hashmap[val] = 1
            else:
                hashmap[val] += 1

        for val in hashmap.values():
            if val % 2 == 0:
                count += val
            else:
                count += val - 1

        for val in hashmap.values():
            if val % 2 != 0:
                count += 1
                break

        return count
    
    def longestPalindrome_better(self, s): 
        hashmap = {} 
        for val in s: hashmap[val] = hashmap.get(val, 0) + 1
        
        count , found_odd = 0, False
        for val in hashmap.values():
            if val % 2 == 0: 
                count += val
            else: 
                found_odd = True
                count += val - 1
        
        if found_odd: 
            count += 1
        
        return count

so = Solution()
r = so.longestPalindrome_better('aabbccc')

print(r)

