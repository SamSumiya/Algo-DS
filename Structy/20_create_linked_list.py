'''
    Create Linked List

    given a list of elements
    the task is to create a linked list from the given elements

    create a head node
    loop through the list and use each element to create a new node
    then we will link the tail to the new node and use next to go to the next node
    finally we can return the head.next to get the ll

'''


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def create_linked_list(values):
    head = Node(None)
    tail = head

    for el in values:
        new_node = Node(el)
        tail.next = new_node
        tail = tail.next

    return head.next
