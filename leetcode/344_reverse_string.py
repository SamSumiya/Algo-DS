'''
344. Reverse String

Intuition:
Since the You must do this by modifying the input array in-place with O(1) extra memory.
We should not create an extra list to store the data
so we will have to swap the elements


Approach: two pointers 
get first idx and last idx of the string
we will just need to swap first and last
and increment the first index and decrement the last index
just keep swapping

'''


class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i, j = 0, len(s) - 1 

        while i < j: 
            s[i], s[j] = s[j], s[i]

            i += 1
            j -= 1
        
        return s