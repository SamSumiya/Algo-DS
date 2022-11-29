

'''
    Get Node Value

    given a ll and index, return the node val at the specified index
    
    approach: iteration 
        1. create a var and set it to 0 
        2. loop through the head
        3. check if the index equals to the var or not
        4. if no, increment the var by 1
        5. if var equals to the index
        6. return the val
        7. return None at the end or just do nothing which will return None


    approach: recrusion
        1. if head is None, then return None
        2. check if index is 0
            a. if it is, then we can return the val at that node
            b. else, we can move on to the next one by move the head to the next and decrement 1 from the index
        
'''


def get_node_value_iter(head, index):
    idx = 0

    while head:
        if idx == index:
            return head.val
        else:
            idx += 1
            head = head.next
    return None


def get_node_value_recur(head, index):
    if head is None:
        return None

    if index == 0:
        return head.val
    return get_node_value_recur(head.next, index - 1)
