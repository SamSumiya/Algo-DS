'''
206. Reverse Linked List

'''


class Solution(object):
    def reverseList(self, head, new_head = None):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None: return new_head

        next_node = head.next
        head.next = new_head
        
        return self.reverseList(next_node, head) 