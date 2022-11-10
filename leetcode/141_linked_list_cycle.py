'''
141. Linked List Cycle

Approach: Time Complexity O(n) and Space Complexity O(n)

    use node as a key for hashmap
    if there is a same key(node) at any time, we know that we can return true
    else we will return False

'''

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head

        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
        
    def hasCycle_hash(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        hash = {} 

        while head: 

            if head not in hash: 
                hash[head] = head
            else: 
                return True
            head = head.next 
        return False