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
