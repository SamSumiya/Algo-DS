'''
142. Linked List Cycle II



'''


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        my_list = set()
        curr = head

        while curr: 
            if curr not in my_list:
                my_list.add(curr)
            else: 
                return curr
            curr = curr.next

        return None
