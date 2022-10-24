'''
    Tree Sum 

    given a binary tree
    the function should return the sum of each exsting node

    approach: 
        use a depth first or breadth first traverse and get the value back

'''


def tree_sum(root):
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
