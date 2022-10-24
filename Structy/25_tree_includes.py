'''

    Tree Includes

    given a binary tree if there is a value that matches the target return True
    else return False

    Approach: depth first traverse iteration


'''


def tree_includes(root, target):
    if root == None:
        return False
    stack = [root]

    while stack:
        current = stack.pop(0)
        if current.val == target:
            return True

        if current.left:
            stack.append(current.left)
        if current.right:
            stack.append(current.right)

    return False
