'''
    Linkedin List Values

    given a linkedin list and insert the values into a list
    return the list


    approach: iteration
        0. create an empty list
        1. loop througth the ll
        2. add each val to the empty list
        3. return the list at the end

    approach: recursion
        1. base case: if ll reaches None
        2. return []
        3. put the current val inside of a list + the function with next node as arg


'''


def linked_list_values_iter(head):
    op = []

    while head:
        op.append(head.val)
        head = head.next

    return op


def linked_list_values_recur(head):
    if head is None:
        return []

    return [head.val] + linked_list_values_recur(head.next)
