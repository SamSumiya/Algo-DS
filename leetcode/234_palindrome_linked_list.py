'''
234. Palindrome Linked List

Approach: stored values in a list

this is probably is the easiest approach. 
we will just need to store each value in a list and compare the list with its reversed version

'''


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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

    def is_palindrome_o1(self, head):
        mid_point_to_end = self.mid_point_to_end(head)
        reversed_second_half = self.reverse_linked_list(mid_point_to_end.next)
        first_position = head
        reversed_position = reversed_second_half

        while reversed_position:
            print(first_position.val, reversed_position.val)
            if first_position.val != reversed_position.val:
                return False
            first_position = first_position.next
            reversed_position = reversed_position.next

        return True

    def mid_point_to_end(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            fast = fast.next.next
            slow = slow.next
        return slow

    def reverse_linked_list(self, head, new_head=None):
        if head is None:
            return new_head

        next_node = head.next
        head.next = new_head

        return self.reverse_linked_list(next_node, head)


one = ListNode('1')
two = ListNode('2')
two_1 = ListNode('2')
one_1 = ListNode('1')

one.next = two
two.next = two_1
two_1.next = one_1
one_1.next = None

ss = Solution()
r = ss.is_palindrome_o1(one)

print(r)
