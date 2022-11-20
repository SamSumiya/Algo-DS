'''
https://practice.geeksforgeeks.org/problems/delete-without-head-pointer/1?page=1&category[]=Linked%20List&sortBy=accuracy

'''


class Solution:
    #Function to delete a node without any reference to head pointer.
    def deleteNode(self,curr_node):
        curr_node.data = curr_node.next.data
        curr_node.next = curr_node.next.next

