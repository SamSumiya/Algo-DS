'''
    Zipper List 

    given two linked lists
    merge them one by one and create a new linkedin list 

    1 -> 2 -> 3
    a -> b -> c 
    1 -> a -> 2 -> b -> 3 -> c


    approach: iteration
        since we need to pick one val each from 2 linked lists, we can use count and % to get 0 or 1 to get values from ll_1 or ll_2
        we need to copy ll_1 so we can modify head_1 to zip the two lists together
        1. dummy_1 has to be less than 1 so we can avoid the duplicate for the first node value
        2. another thing is that next will give us the next value instead of the entire ll which is the key to solve this issue in iterative way
        3. note that head_1 or head_2 might have some remaining values so we should capture it before return it

    
    approach: recursion
        basecase will be either ll1 or ll2 is none, when it becomes none we can return ll1 or ll2 which will just add the remain leftovers to head_1
        keep getting the next ll1 and ll2
        modify ll1 and ll2 
            1. ll1 is easy we just need to set ll1.next = ll2 
            2. the tricky part is ll2
                a. 1 -> 2 and a -> b case 
                b. ll1 will be 1 -> a -> b
                c. then we will need to update b back to 2
                d. so we can think about using the recursive call and pass the next nodes to it
                e. then ll2 will be updated to a -> 2
                f. and since ll1.next is ll2
                g. the outcome will be 1 -> a -> 2 
                h. then we will continue the process
                
'''


def zipper_lists_iter(head_1, head_2):
    count = 0
    dummy = head_1
    next_1 = head_1.next

    while next_1 and head_2:
        if count % 2 == 0:
            dummy.next = head_2
            head_2 = head_2.next
        else:
            dummy.next = next_1
            next_1 = next_1.next
        count += 1
        dummy = dummy.next

    if head_1:
        dummy.next = next_1
    if head_2:
        dummy.next = head_2

    return head_1


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def zipper_lists_iter_newhead(head_1, head_2):
    new_head = Node(None)
    dummy = new_head
    count = 0

    while head_1 and head_2:
        if count % 2 == 0:
            dummy.next = head_1
            head_1 = head_1.next
        else:
            dummy.next = head_2
            head_2 = head_2.next
        dummy = dummy.next
        count += 1

    if head_1:
        dummy.next = head_1
    if head_2:
        dummy.next = head_2

    return new_head.next


def zipper_lists_recur(head_1, head_2):
    if head_1 is None:
        return head_2
    if head_2 is None:
        return head_1

    next_1 = head_1.next
    next_2 = head_2.next
    head_1.next = head_2
    head_2.next = zipper_lists_recur(next_1, next_2)
    return head_1
