'''
    Depth First Values

    given a binary tree
        We will need to implement a stack to achieve first in first out pattern
        so we can use an array to help us to do that
        we known that each node has a value or might have left or right node to it
        so we should get val from each node and move on to the next node if applicable
        the isssue is that how can we also store the next nodes and keep it in a stack? 
        what we can do is push each node to an array and get the last node by poping the array
        so what happends is that whatever comes first will be stored at the end of the array and gets popped first


'''


def deptg_first_values_iter(root):
    if root is None: return []
    stack = [root]
    output = []

    while stack:
        current = stack.pop()
        if current.right:
            stack.append(current.right)
        if current.left:
            stack.append(current.left)
        output.append(current.val)
    return output


