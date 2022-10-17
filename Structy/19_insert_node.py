'''
    Insert Node

    We need to insert a new node with the vlaue into the list at the specified index
    consider head as index 0 

    Approach: iterative
    we will need a count and set it at 0 initially
    every loop we will need to increment the index up by 1
    when the index equals to the specified index
    we will need to creat a new node and link it to the previous linked list and get the linked list after
    previous ll 
    when 

'''


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def insert_node(head, value, index):
    count = 1
    tail = head
    new_node = Node(value)
    if index == 0:
        new_node.next = head
        return new_node
    while tail:
        if count == index:

            rest = tail.next
            tail.next = new_node
            tail.next.next = rest

        tail = tail.next
        count += 1

    return head
