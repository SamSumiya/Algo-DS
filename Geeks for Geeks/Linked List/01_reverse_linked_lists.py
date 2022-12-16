class Solution:
    # Function to reverse a linked list.
    def reverseList(self, head):
        new_head = None

        while head:
            next = head.next
            head.next = new_head
            new_head = head
            head = next

        return new_head
