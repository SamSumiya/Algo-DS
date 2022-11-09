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

    approach: recursion 1
        basecaes: head.next is None then we can return True

        get the value of the current node and next node
        compare it 
        if nothing found: we can move onto the next node
    
    approach: recursion 2
        base case would be when the head reaches the end
        additionally we will add a prev_val as an arg
        so we can check if prev_val is None or prev_val equals to the current head val or not
        if it does, we will just move to the next node
        until the if statement returns false
'''


def is_univalue_list_iter(head):

    while head.next != None:
        if head.val != head.next.val:
            return False
        head = head.next

    return True


def is_univalue_list(head, prev_val=None):
    tail = head

    while tail:
        if prev_val is None:
            prev_val = tail.val
        else:
            if prev_val != tail.val:
                return False
            prev_val = tail.val
        tail = tail.next
    return True


def is_univalue_list_recur_b(head):
    if head.next is None:
        return True

    next_node = head.next
    if head.val != head.next.val:
        return False

    return is_univalue_list_recur_b(next_node)


def is_univalue_list_recur(head, prev_val=None):
    if head is None:
        return True

    if prev_val == None or head.val == prev_val:
        prev_val = head.val
        return is_univalue_list_recur(head, prev_val)
    else:
        return False
