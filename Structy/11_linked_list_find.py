'''

    Linkedin List Find

    given a ll, return true if the target exists else return false

    approach: iteration 
        1. loop through the ll 
        2. if value equals to the target
        3. return true
        4. return false at the end 
    
'''


def linked_list_find_iter(head, target):

    while head:
        if head.val == target:
            return True
        head = head.next
    return False


def linked_list_find_recur(head, target):
    if head is None:
        return False

    if head.val == target:
        return True

    return linked_list_find_recur(head.next, target)
