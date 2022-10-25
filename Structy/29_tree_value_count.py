'''
    Tree Value Count 


    given a binary tree and a target
    return a count if the value equals to the target

    approach: recursion 
        base case return count which is 0 
        if node.val == target
            count += 1
        and recursively call left and right
        at the end of each function call 
        we will return count + left and right
    
'''


def tree_value_count_recur(root, target, count=0):
    if root is None:
        return count

    # if root.left is None and root.right is None:
    #   return root.val
    if root.val == target:
        count += 1
    left = tree_value_count_recur(root.left, target)
    right = tree_value_count_recur(root.right, target)

    return count + left + right
