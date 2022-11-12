'''
142. Linked List Cycle II



'''


class Solution(object):
    def detectCycle_1(self, head):
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

    def detectCycle_2(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return

        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                break

        if not fast or not fast.next:
            return

        slow2 = head

        while slow.next:
            if slow == slow2:
                return slow
            slow = slow.next
            slow2 = slow2.next
