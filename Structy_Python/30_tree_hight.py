'''
    How Hign 

    given a binary tree 
    return the level of the tree 
    if the tree is empty return -1 


    approach: recursion 
        when the node is empty we will need to return -1 to hit the base case 
        then we recusively add the 1 to each branch and compare the two side and get the max one from it

'''


def how_high(node):
    if node is None:
        return -1

    left = how_high(node.left)
    right = how_high(node.right)

    return 1 + max(left, right)

