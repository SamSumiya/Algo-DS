'''
    Depth First Values

    given a binary tree 
    we will need to traverse the tree and get values from left to right depth first
    and store it in a list
    
'''

def deptg_first_values(root): 
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