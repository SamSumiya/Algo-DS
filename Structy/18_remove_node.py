'''
    Remove Node

    given a linked list and remove the target value from it.
    if there are multiple nodes match the value
    we will only delete the first one we encounter

    approach: iteration
        iterate the linked list
        if the value matches the node
        we will skip the node and set the next to the remainder.next

        since we cannot modify the original head
        we need to create a copy of the head for manipulation
        additonally we also need to have access to the previous and next values on each nodes iteration
        and these nodes will be shorter everytime so we can move to the end of the linked list
        if we find the match to the target value
        we can just simply connect the previous to the current linked list next node 
        and then break it (Since we no longer need to process the remaining data)
        ** edge case ** 
        when the head.val immediately equals to the target
        we can just return whatever comes after the head
    
    approach: recursive
        we will need to skip one node
        since we are in a recurision, we can chain up the nodes by using the original linked list


'''


def remove_node(head, target_val):
    if head.val == target_val:
        return head.next

    copy = head

    while copy:
        if copy.val == target_val:
            second_copy.next = copy.next
            break

        second_copy = copy
        copy = copy.next

    return head
