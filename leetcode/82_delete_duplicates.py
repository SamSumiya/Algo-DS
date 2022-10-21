'''
    Delete Duplicates

    given a sorted linked list
    we will need to delete all nodes if there are duplicates
    1 -> 1 -> 2 will be 2
    [1,2,3,3,4,4,5] will be [1,2,5] 

    approch; recursion
    Runtime: 173 ms, faster than 5.13% of Python3 online submissions for Remove Duplicates from Sorted List II.
    Memory Usage: 14 MB, less than 30.51% of Python3 online submissions for Remove Duplicates from Sorted List II.
        first check if the first val equals to the next val
            if it does then we will assign the head to the function call with ll that has two nexts
                also we can get the prev_val from the current val
            then we can check if the prev_val equals to the current.val or not 
            if it does, then we can shorten the head by passing head.next
            if it does not, then we can finally just get head.next = f(head.next)
            and reuturn the head
        ** in case of last val. we can get it at the end of the recursive call when the base case becomes false. 
        we can return the head at that point which should be the last node. 
'''
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode], prev_val = None) -> Optional[ListNode]:
        if head is None or head.next is None: return head
        # prev_val = None
        
        if head.val == head.next.val:
            prev_val = head.next.val
            head = Solution.deleteDuplicates(self, head.next.next, prev_val)
        if head and head.val == prev_val:
            head = Solution.deleteDuplicates(self, head.next, prev_val)
        if head: 
            head.next = Solution.deleteDuplicates(self, head.next, prev_val)
    
        return head