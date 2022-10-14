'''
    is univalue list

    given a linked lists with value(s)
    return true if the value(s) are the same 
    return false if the value(s) are not the same


    approach: iteration
        iterate through the linked list 
        1. get the current node value 
        2. get the next node value 
        3, compare the those
        ** the last node will be compare to None ** 
        make sure the head.next does not equal to None

    approach: recursion 
        basecaes: head.next is None then we can return True

        get the value of the current node and next node
        compare it 
        if nothing found: we can move onto the next node
'''


def is_univalue_list_iter(head):

    while head.next != None:
        if head.val != head.next.val:
            return False
        head = head.next

    return True


def is_univalue_list_recur(head):
    if head.next is None:
        return True

    next_node = head.next
    if head.val != head.next.val:
        return False

    return is_univalue_list_recur(next_node)
