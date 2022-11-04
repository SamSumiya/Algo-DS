from typing import Optional

'''
[1 2 3 4 5]
3 4 5 


    Approach: iterative (Brute force)
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

    approach: iterative 
        use two variables to modify head
        one does not modify the head, but we should use it for second variabe to get to the right index
        if the num is 2: 
            then we can just modify the first linked list by shortening it
            then the remaining length of first_val can be used as a lenght to shorten the second_variable
            *** however, we need to pay attention to the one edge case which is what if there is only one node and num is 1
            this should return None so we can basically say if var_1 is None(after the iteration), we will just return head.next
        for the rest
            we can use val_1 to iterave and skip the node when val_1 is None
        return the head at the end

'''

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd_bf(self, head: Optional[ListNode], n: int, new_head = None, output = None) -> Optional[ListNode]:
        
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


    def removeNthFromEnd(self, head: Optional[ListNode], n: int, new_head = None, output = None) -> Optional[ListNode]:
        fast, slow = head, head
        for _ in range(n): fast = fast.next
        if fast is None: return head.next
        while fast.next: fast, slow = fast.next, slow.next
        slow.next = slow.next.next
        return head