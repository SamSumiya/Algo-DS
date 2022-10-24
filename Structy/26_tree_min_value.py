'''
    Tree min Value

    given a binary tree
    find a value that is the smallest

    approach: depth first iteration 
        set a value to float('inf') to be the min value
        then loop through the tree 
            if there is a value that is greater than the min value
            update it to that value
    
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
