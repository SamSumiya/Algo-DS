'''
    Breadth First Values

    givne a binary tree 
    our task is get values from each level of the tree 

    approach: iteration

        on the top level, we can get the value and store it into the output list
        then we can get the its left and right values if applicable
        then we can a list to store the next node to the current node
        we will need to get the first node from the list so it works like a queue

'''


def breadth_first_values(root):
    if root == None:
        return []
    queue = [root]
    output = []
    output.append(root.val)

    while queue:
        current = queue.pop(0)
        if current.left:
            queue.append(current.left)
            output.append(current.left.val)
        if current.right:
            queue.append(current.right)
            output.append(current.right.val)

    return output


def breadth_first_values(root):
    if root is None:
        return []

    queue = [root]
    output = []

    while queue:
        current = queue.pop(0)
        output.append(current.val)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return output
