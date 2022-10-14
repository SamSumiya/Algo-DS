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


'''


def is_univalue_list_iter(head):

    while head.next != None:
        if head.val != head.next.val:
            return False
        head = head.next

    return True
