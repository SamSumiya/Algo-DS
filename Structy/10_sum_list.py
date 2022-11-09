'''
    Sum LL

    given a ll and sum all the enumeric values together

    Approach: iteration 

        1. create a variable starts from 0 
        2. loop through the ll 
        3. add the enumeric value on each node to the var 
        4. return the var at the end 


    approach: recursion
        1. basecase: when head reaches none we can return 0 
        2. add value on each node
        3. use the next node as the arg in the same function

'''


def sum_list_iter(head):
    op = 0

    while head:
        op += head.val
        head = head.next

    return op


def sum_list_recur(head):
    if head is None:
        return 0
    return head.val + sum_list_recur(head.next)
