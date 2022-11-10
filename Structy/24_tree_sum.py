'''
    Tree Sum 

    given a binary tree
    the function should return the sum of each exsting node

    approach: 
        use a depth first or breadth first traverse and get the value back

'''


def tree_sum_df_iter(root):
    output = 0
    if root is None:
        return output
    stack = [root]

    while stack:
        current = stack.pop()
        output += current.val

        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    return output


def tree_sum_dp_recur(root):
    if root is None:
        return 0

    left = tree_sum_dp_recur(root.left)
    right = tree_sum_dp_recur(root.right)

    return root.val + left + right


def tree_sum_bp_iter(root):
    if root is None:
        return 0
    output = 0
    queue = [root]

    while queue:
        current = queue.pop(0)
        output += current.val

        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return output
