'''
    Depth First Values

    
    Approach: iteration
        We will need to implement a stack to achieve first in first out pattern
        so we can use an array to help us to do that
        we known that each node has a value or might have left or right node to it
        so we should get val from each node and move on to the next node if applicable
        the isssue is that how can we also store the next nodes and keep it in a stack? 
        what we can do is push each node to an array and get the last node by poping the array
        so what happends is that whatever comes first will be stored at the end of the array and gets popped first

    Approach: recursion
        we will need to traverse from the root to each leaf
        the return value should be in a list and populated with value from each leaf
        what we can do is that since recusion is already like a stack
        what we can do is that get the value from each node when we reach the base case which is root is None
        the return value should be compatible with the list that is going to store the values,
        so we will need to return [] 




'''


def deptg_first_values_iter(root):
    if root is None:
        return []
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


def depth_first_values_recur(root):
    if root is None:
        return []

    left = depth_first_values_recur(root.left)
    right = depth_first_values_recur(root.right)

    return [root.val] + left + right
