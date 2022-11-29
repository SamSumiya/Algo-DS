'''
    Merge Lists

    given two sorted lls, we will need to compare the values of both sides and return a sorted list



    approach: iteration
        We need to have a have a base ll to start, since we are not sure which one should we use to start
        it would be more efficient to start from scratch which is a brand new linked list
        then we can simply compare the node1 to node2 and assign the value of the smaller one to new_head
        continue the process and move the assinged ll to the next node as well as tail to the next
        at the end, assign the left over ll to the tail before return the linked list
        ** Since we start from a linked list with the value of None, so we have to return the value from the node next to the none value
    
    approach: recurive
        Building a new linkedin list always need steps involving move the ll to the next node
        basecase would be if head_1 or head_2 becomes none then we can return head_2 or head_1

        in a if statement comparing two nodes
        we need to think about how to build the next ll without the current node that we are on
        so for instance, if we are added new node to linkedin list 1, then we should not include linkedin list 1 in the next function
        by doing this, we are moving the node from 1 to the next one 2. 
        we are also updating the head_1 and head_2 and also keeping the rest of the nodes in next_1 and next_2
        since this is a recursive call, we will need to return the ll from this functional call and move on to the next 

'''


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def merge_lists_iter(head_1, head_2):
    new_ll = Node(None)
    tail = new_ll

    while head_1 and head_2:
        if head_1.val < head_2.val:
            tail.next = head_1
            head_1 = head_1.next
        else:
            tail.next = head_2
            head_2 = head_2.next
        tail = tail.next

    if head_1:
        tail.next = head_1
    if head_2:
        tail.next = head_2

    return new_ll.next


def merge_lists(head_1, head_2):
    if head_1 is None:
        return head_2
    if head_2 is None:
        return head_1

    if head_1.val < head_2.val:
        next_1 = head_1.next
        head_1.next = merge_lists(next_1, head_2)
        return head_1
    else:
        next_2 = head_2.next
        head_2.next = merge_lists(head_1, next_1)
        return head_2
