'''
    Tree min Value

    given a binary tree
    find a value that is the smallest

    approach: depth first iteration 
        set a value to float('inf') to be the min value
        then loop through the tree 
            if there is a value that is greater than the min value
            update it to that value
    
    approach: depth first recursion
        at the end, we return a float('inf')
        so our job is to hit the base case for each branch and return the smaller nunber
        so we should go left and right and each branch will return a number
        at the end, we should get the left and right branchs' smallest number
    
'''


def tree_min_value_df_iter(root, min_val=float('inf')):

    stack = [root]

    while stack:
        current = stack.pop()
        if current.val < min_val:
            min_val = current.val
        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    return min_val


def tree_min_value_dp_recur(root):
    if root is None:
        return float('inf')

    left = tree_min_value_dp_recur(root.left)
    right = tree_min_value_dp_recur(root.right)

    return min(root.val, left,  right)
