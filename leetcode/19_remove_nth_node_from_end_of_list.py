from typing import Optional

'''

    Approach: iterative 
        [there is a nested while loop so the time complexity O2 ]
        this is a little brute force way of solving this challenge
        I first reversed the linked list and then 
        use a variable to keep track of the count
        when the count == n
        then I will skip one node by using sentinel approach 
        there are two cases that I will need to cover
            1. when n == 1
                in this case, I cannot directly manipulate the linked list and make it one node shorter
                so i will need to create a sentinel node LinkNode(0, new_head)
                and then loop through the this sentinel node and try to reverse it back to the right order
            2. when n is greater than 1
                i will need to remove the node and also keep track of the previous node 
                so before each iteration, I can use 
                current = tail
                tail = tail.next 
                so the current will hold the previous node value
                which helps me to keep track of the right order


'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int, new_head = None, output = None) -> Optional[ListNode]:
        
        while head: 
            next_node = head.next
            head.next = new_head
            new_head = head
            head = next_node 

        counter = 1
        copy = new_head
        # sentinel = ListNode(0, new_head)
        while copy: 
            if n == 1: 
                sentinel = copy.next
                while sentinel: 
                    next_node = sentinel.next
                    sentinel.next = output
                    output = sentinel 
                    sentinel = next_node
                return output

            if counter == n:
                prev_node.next = copy.next
                # break
            
            prev_node = copy
            counter += 1
            copy = copy.next
        while new_head: 
            next_node = new_head.next
            new_head.next = output
            output = new_head 
            new_head = next_node
        return output