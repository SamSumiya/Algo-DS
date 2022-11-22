# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow, fast, tail =  head, head.next, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = slow.next
        new_head = slow.next =  None

        while second_half:
            next_node = second_half.next
            second_half.next = new_head
            new_head = second_half 
            second_half = next_node
        

        while new_head: 
            next_tail = tail.next 
            next_new_head = new_head.next
            tail.next = new_head 
            new_head.next = next_tail
            tail = next_tail
            new_head = next_new_head