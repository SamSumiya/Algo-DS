'''
    Add Lists

    given two linked list
    we will need to add the value from both ll and create a new linked list
    there will be cases that one linked list is longer or shorter than another
    and when add one and another the value will exceed 9 which means that the extra digit will have to 
    be career over the next digit

    approch: iterative native ?
        since it is very similar to a sum
        my approach is create a two str of the values from each linked list 
        and convert it to two numbers before we add them together.

        lastly, convert the integer to a str and use node to create a linked list

    approach: iterative
        since we might have a carry over 1 in cases of 8 + 9
        so we should also cover that case by adding it to the while loop to keep the loop going
        we will always get values from the two list and add them together to see what the sum is
        also consider the carry
        if the carry is bigger, we don't need to mannually extract the one digit from the sum
        we can simply add one to the carry and change the carry to 0 when the sum is less than 9
        we can use modulo 10 to the first digit 

    approachl: recursion
        we need to create a new linked list and it can be the first node which is head 
        then we will need to add the next sum to the next node
        the carry over and be dealt in args and use a if statement to either keep it or delete it
        if key here is that every function call, we need to provide some values to val_1 and val_2 so we wont run into issues as 
        None + a number


'''


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def add_lists_iter_0(head_1, head_2):
    head = Node(None)
    tail = head
    n1 = ''
    n2 = ''
    while head_1:
        n1 += str(head_1.val)
        head_1 = head_1.next

    while head_2:
        n2 += str(head_2.val)
        head_2 = head_2.next

    num = int(n1[::-1]) + int(n2[::-1])
    string_num = str(num)
    print(num)
    for el in string_num[::-1]:
        node = Node(el)
        tail.next = node
        tail = tail.next

    return head.next


def add_lists(head_1, head_2):
    head = Node(None)
    tail = head
    carry = 0

    while head_1 or head_2 or carry == 1:
        val_1 = head_1.val if head_1 else 0
        val_2 = head_2.val if head_2 else 0
        sum = val_1 + val_2 + carry

        carry = 1 if sum > 9 else 0
        digit = sum % 10

        node = Node(digit)
        tail.next = node
        tail = tail.next

        if head_1:
            head_1 = head_1.next
        if head_2:
            head_2 = head_2.next

    return head.next


def add_lists_recur(head_1, head_2, carry=0):
    if head_1 is None and head_2 is None and carry == 0:
        return None

    if head_1:
        val_1 = head_1.val
    else:
        2 cxl
        val_1 = 0
    if head_2:
        val_2 = head_2.val
    else:
        val_2 = 0
    sum = val_1 + val_2 + carry
    next_carry = 1 if sum > 9 else 0
    digit = sum % 10
    node = Node(digit)

    if head_1:
        next_1 = head_1.next
    else:
        next_1 = None
    if head_2:
        next_2 = head_2.next
    else:
        next_2 = None

    node.next = add_lists_recur(next_1, next_2, next_carry)
    return node
