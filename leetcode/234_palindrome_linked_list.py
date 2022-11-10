'''
234. Palindrome Linked List

Approach: stored values in a list

this is probably is the easiest approach. 
we will just need to store each value in a list and compare the list with its reversed version

'''



class Solution(object):
    def isPalindrome_list(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        stored_values = []

        while head: 
            stored_values.append(head.val)
        
            head = head.next
        
        return stored_values == stored_values[::-1]