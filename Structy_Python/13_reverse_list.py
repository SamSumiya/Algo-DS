'''

    Reverse Linkedin List


    approach: iteration 
        we will need to change the next from a -> b to None <- a ..., so we need to a new variable and set its value to None
        after that we need to modify the head so we will need to keep the reference of the rest of the ll
        head will have new values ( ** head will no longer be the original head ** )
        
        1. we need to create a new variable and set it value to none
        2. modify the first to point at none
        3. after that we can basically set the new_head to this modify head 
        4. since we still need to iterate through the head from the next node
        5. we will need to set the head to the next node
    

    approach: recurision 
        0. add a new arg new_head and set it to none
        1. base case: if head is none then we will return new_head
        2. head next will be new_head
        3. get the rest of linked list
        4. new_head will be the current head which points to None at the beginning
        4. return the value that head will be the next_node and new_node will be node
'''


def reverse_list_iter(head):
    reverse_list = None

    while head:
        next_node = head.next
        head.next = reverse_list
        reverse_list = head
        head = next_node

    return reverse_list


def reverse_list_recur(head, new_head=None):
    if head is None:
        return new_head

    next_node = head.next
    head.next = new_head
    new_head = head

    return reverse_list_recur(next_node, new_head)
