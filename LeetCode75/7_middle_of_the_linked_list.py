'''

876. Middle of the Linked List
'''


class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head

        while fast and fast.next: 
            fast = fast.next.next
            slow = slow.next
        
        return slow