'''
    Remove Duplicates from Sorted List

    given a sorted list, we will need to delete the all the duplicates from it

    for instance: 
        1 -> 1 -> 2 will be 1 -> 2
        1 -> 1 -> 1 will just 1

    approch: iterative
        we will compare the first and second value 
        if there is a match
            we will skip the next one
        else (must have else)
            if no else: then tail will be altered
            lets say 1 -> 1 -> 1
            so befor eles: my current tail should be 1 
            but if there is else
                tail = tail.next
                it will give me  1 -> 1 instead
        we can just compare the first value and second value


    
    approach: recursive
        I will need to capture the previous node value and current node value
        so I used an additional arg prev_val and set it to None as inital value
        everytime, I will set the prev_val to the current val and current_val is from the next node
        it allows me to compare the two vals
        so if the prev_val == node.val
            I will just move the node to the next node: 1 -> 1
                then the new_head will just be the next one which is 1
        else: 
            I will just move the head to the next one without removing the head


'''

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode], prev_val=None) -> Optional[ListNode]:
        if head is None:
            return

        next_node = head.next
        current_val = head.val
        if current_val == prev_val:
            head = Solution.deleteDuplicates(self, next_node, current_val)
        else:
            head.next = Solution.deleteDuplicates(self, next_node, current_val)
        return head

## wrong way
#         if head is None: return None

#         next_node = head.next
#         current_val = head.val

#         if prev_val == current_val:
#             head = head.next

#         head.next = Solution.deleteDuplicates(self, next_node, current_val)
#         return head


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail = head 
        
        while tail and tail.next:
            Next_Node = None
            if tail.next.val == tail.val: 
                Next_Node = tail.next.next
                # tail.next = tail.next.next
                tail.next = Next_Node
            else:
                tail = tail.next
    
        return head