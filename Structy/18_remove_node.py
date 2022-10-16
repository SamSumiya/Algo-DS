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
        additonally we also need to have access to the first and second values on each nodes
        and these nodes will be shorter everytime so we can move to the end of the linked list
        if we find the match to the target value
        we can just simply connect the current node.next to the copy.next 
        and break it (Since we no longer need to process the remaining data)
        ** edge case ** 
        when the head.val immediately equals to the target
        we can just return whatever comes after the head 

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
