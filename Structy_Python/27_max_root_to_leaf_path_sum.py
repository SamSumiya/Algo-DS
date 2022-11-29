'''
    Max root to leaf path sum

    given a bianry tree 
    get the sum from a branch that has the biggest sum 


    approach: recursion

        base case is the -inf to compare when is is null node
        since we should compare the left and right side so we should avoid the node to go down the path to null node
        once get the all leaves node values back
        we then can go up one level in the stack which is going to be the parent node of the leave nodes
        then we will add the current node value and the max of the two values
        then we can just continue this recursive process until the end

'''


def max_path_sum(root):
    if root is None:
        return float('-inf')

    if root.left is None and root.right is None:
        return root.val

    left = max_path_sum(root.left)
    right = max_path_sum(root.right)

    return root.val + max(left, right)
