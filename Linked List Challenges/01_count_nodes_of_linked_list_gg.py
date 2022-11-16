'''
https://practice.geeksforgeeks.org/problems/count-nodes-of-linked-list/1?page=1&category[]=Linked%20List&sortBy=accuracy

Approach: iteration 


'''


# Linked list class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


class Solution:

    # Function to count nodes of a linked list.
    def getCount_iter(self, head_node):
        count = 0

        while head_node:
            count += 1
            head_node = head_node.next

        return count

    def getCount(self, head_node, count = 0):
        if head_node is None: return count 
        count += 1 if head_node else 0 
        
        return self.getCount(head_node, count)

