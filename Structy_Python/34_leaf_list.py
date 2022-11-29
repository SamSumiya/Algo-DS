'''
leaf list
Write a function, leaf_list, that takes in the root of a binary tree and returns a list containing the values of all leaf nodes in left-to-right order.

Approach: recursion 
    have an output input array 
    and only push the value when the left and right values are none
    then keep the recursive calls on both left and right side
    so return the output for each function call

'''


def leaf_list(root, output=[]):
    if root is None:
        return []

    if root.left is None and root.right is None:
        output.append(root.val)

    leaf_list(root.left, output)
    leaf_list(root.right, output)

    return output
